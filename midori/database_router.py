import hashlib

class ShardedRouter:
    def db_for_read(self, model, **hints):
        if model.__name__ == "Page":
            if hints.get('instance'):
                url = hints.get('instance').url
                return self.get_shard_alias(url)
        return None

    # def db_for_write(self, model, **hints):
    #     if model.__name__ == "Page":
    #         instance = hints.get('instance')
    #         if instance and hasattr(instance, 'url'):
    #             url = instance.url
    #             return self.get_shard_alias(url)
    #     return None

    def get_shard_alias(self, url):
        hash = hashlib.sha256(url.encode()).hexdigest()
        shard = int(hash, 16) % 4
        return f"shard{shard}", hash
    
    def get_shard_alias_from_hash(self, hash):
        shard = int(hash, 16) % 4
        return f"shard{shard}"
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db in ["shard0", "shard1", "shard2", "shard3"]:
            return True
        return None