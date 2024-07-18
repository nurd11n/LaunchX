# from django.views.decorators.cache import cache_page
# from django.utils.decorators import method_decorator
# import logging

# import re
# from django.core.cache import cache
# from django.conf import settings

# from apps.history.models import *
# from django.dispatch import receiver
# from django.db.models.signals import post_save

# logger = logging.getLogger('product')


# class CacheMixin:
#     @method_decorator(cache_page(60 * 15))
#     def dispatch(self, *args, **kwargs):
#         logger.debug(f"Вызван метод {self.request.method} для {self.__class__.__name__}")
#         return super().dispatch(*args, **kwargs)


# def delete_cache_pattern(pattern: str):
#     cache_keys = cache._cache.keys()
#     regex = re.compile(pattern)
#     keys_to_delete = [key for key in cache_keys if regex.match(key)]

#     for key in keys_to_delete:
#         cache.delete(key)


# def delete_cache(key_prefix: str):
#     keys_pattern = f"views.decorators.cache.cache_.*.{key_prefix}.*.{settings.LANGUAGE_CODE}.{settings.TIME_ZONE}"
#     delete_cache_pattern(keys_pattern)


# @receiver(post_save, sender=Year)
# def delete_caches_service(sender, instance, created, **kwargs):
#     print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
#     if created:
#         delete_cache(instance.CACHE_KEY_PREFIX)


# @receiver(post_save, sender=CollectionImage)
# def delete_caches(sender, instance, created, **kwargs):
#     print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
#     if created:
#         delete_cache(instance.CACHE_KEY_PREFIX)


# @receiver(post_save, sender=PostImage)
# def delete_caches(sender, instance, created, **kwargs):
#     print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
#     if created:
#         delete_cache(instance.CACHE_KEY_PREFIX)


# @receiver(post_save, sender=Post)
# def delete_caches(sender, instance, created, **kwargs):
#     print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
#     if created:
#         delete_cache(instance.CACHE_KEY_PREFIX)


# @receiver(post_save, sender=Category)
# def delete_caches(sender, instance, created, **kwargs):
#     print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
#     if created:
#         delete_cache(instance.CACHE_KEY_PREFIX)


# @receiver(post_save, sender=Collection)
# def delete_caches(sender, instance, created, **kwargs):
#     print(f"Delete cash in {instance.CACHE_KEY_PREFIX}")
#     if created:
#         delete_cache(instance.CACHE_KEY_PREFIX)


