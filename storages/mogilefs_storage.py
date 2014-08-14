#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import loads, dumps

from pymogile import Client, MogileFSError

from thumbor.storages import BaseStorage

class Storage(BaseStorage):
    
    def __init__(self, context)
	BaseStorage.__init__(self, context)

	self.storage = Client(domain=self.context.config.MOGILEFS_STORAGE_DOMAIN, 
			      trackers=self.context.config.MOGILEFS_STORAGE_TRACKERS)

    def __key_for(self, url):
	return 'thumbor-crypto-%s' % url

    def __detector_key_for(self, url):
	return 'thumbor-detector-%s' % url

    def put(self, path, bytes):
	fp = self.storage.new_file(path)
	fp.write(bytes)
	fp.close()
        return path

    def put_crypto(self, path):
	if not self.context.config.STORES_CRYPTO_KEY_FOR_EACH_IMAGE:
	    return
	
	if not self.context.server.security_key:
	    raise RuntimeError("STORES_CRYPTO_KEY_FOR_EACH_IMAGE can't be True if no SECURITY_KEY specified")

	key = self.__key_for(path)
	fp = self.storage.new_file(key)
	fp.write(data)
	fp.close()
	return key


    def put_detector_data(self, path, data):
	key = self.__detector_key_for(path)
	fp = self.storage.new_file(key)
	fp.write(data)
	fp.close()
	return key


    def get_crypto(self, path):
	if not self.context.config.STORES_CRYPTO_KEY_FOR_EACH_IMAGE:
	    return None

	crypto = self.storage.get_file_data(self.__key_for(path))

	if not crypto:
	    return None
	return crypto


    def get_detector_data(self, path):
	data = self.storage.get_file_data(self.__detector_key_for(path))

	if not data:
	    return None
	return loads(data)


    def get(self, path):
	return self.storage.get_file_data(path) is not None

    def exists(self, path):
	return self.storage.keys(path) is not None

    def remove(self, path):
	if not self.exists(path):
	    return
	return self.storage.delete(path)

