# thumbor-mogilefs

MogileFS storage backend for thumbor

## Installation

To install the MogileFS storage backend, mv the mogilefs_storage.py to the
storage directory of thumbor.

Example:

    mv storage/mogilefs_storage.py /usr/local/lib/python2.7/dist-packages/thumbor/storages/


## Configuration

To use it at thumbor enable it as a storage:

    ## The file storage thumbor should use to store original images. This must be the
    ## full name of a python module (python must be able to import it)
    ## Defaults to: thumbor.storages.file_storage
    STORAGE = 'thumbor.storages.mogilefs_storage'

and add the following settings for your storage:

    MOGILEFS_STORAGE_DOMAIN = 'YOUR_DOMAIN'
    MOGILEFS_STORAGE_TRACKERS = [ 'TRACKER1:PORT', 'TRACKER2:PORT' ]
