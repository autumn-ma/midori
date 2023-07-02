from django.conf import settings
from django.db import connection
import typing

from pages.models import GlobalIncrementTracker

def get_next_auto_id_across_shard(table_name: str) -> int:
    """
    Get the next auto-increment primary key value across all shards.
    params:
        db: the database alias
        table_name: the table name
    """

    # Get all the shard aliases
    shard_aliases = settings.DATABASES.keys()

    # Get the next auto-increment primary key value for each shard depending on the shard engine
    next_values = []
    for shard_alias in shard_aliases:
        engine = settings.DATABASES[shard_alias]['ENGINE']
        if 'sqlite3' in engine:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT seq + 1 FROM sqlite_sequence WHERE name='{table_name}'")
                next_value = cursor.fetchone()[0]
                next_values.append(next_value)
        elif 'mysql' in engine:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA = '{shard_alias}' AND TABLE_NAME = '{table_name}'")
                next_value = cursor.fetchone()[0]
                next_values.append(next_value)
        elif 'postgresql' in engine:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT nextval(pg_get_serial_sequence('{table_name}', 'id'))")
                next_value = cursor.fetchone()[0]
                next_values.append(next_value)
        else:
            raise Exception(f"Engine {engine} not supported")
        
    # Return the max value
    return max(next_values)

    
def save_id_to_global_increment_tracker(table_name: str, id: int) -> None:
    """
    Save the id to the global increment tracker table.
    params:
        table_name: the table name
        id: the id
    """
    GlobalIncrementTracker.objects.filter(table_name=table_name).update(last_id=id)

def get_or_create_id_from_global_increment_tracker(table_name:str) -> int:
    """
    Get or Create the id from the global increment tracker table.
    params:
        table_name: the table name
        id: the id
    """
    try:
        return GlobalIncrementTracker.objects.get(table_name=table_name).last_id
        
    except GlobalIncrementTracker.DoesNotExist:
        return GlobalIncrementTracker.objects.create(table_name=table_name).last_id
    
