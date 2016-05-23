from __future__ import absolute_import
__all__ = []

from .browser import BrowserObject
from .interfaces import InterfaceObject

def get_interface(bucket_name,
                  ACCESS_KEY=False,
                  SECRET_KEY=False,
                  endpoint_url=None,
                  verbose=True):
    '''Return an interface to S3.

    Parameters
    ----------
    bucket_name : str
        Bucket to use
    ACCESS_KEY : str
        The S3 access key
    SECRET_KEY : str
        The S3 secret key
    url : str
        The URL for the S3 gateway

    Returns
    -------
    cci  : cottoncandy.InterfaceObject
        Cottoncandy interface object
    '''
    from .interfaces import DefaultInterface

    if (ACCESS_KEY is False) and (SECRET_KEY is False):
        from .utils import get_keys
        ACCESS_KEY, SECRET_KEY = get_keys()

    interface = DefaultInterface(bucket_name,
                                 ACCESS_KEY,
                                 SECRET_KEY,
                                 endpoint_url,
                                 verbose=verbose)
    return interface


def get_browser(bucket_name,
                ACCESS_KEY=False,
                SECRET_KEY=False,
                endpoint_url=None):
    """Get an object that allows you to tab-complete your
    way through your objects

    Parameters
    ----------
    bucket_name : str
        Bucket to use
    ACCESS_KEY : str
        The S3 access key
    SECRET_KEY : str
        The S3 secret key
    endpoint_url : str
        The URL for the S3 gateway

    Returns
    -------
    ccb  : cottoncandy.BrowserObject
        Cottoncandy browser object

    Example
    -------
    >>> browser = cloud.get_browser('anunez_raid')
    >>> browser.auto.k<TAB-COMPLETION>
    browser.auto.k1
    browser.auto.k8

    >>> browser.auto.k8.anunez.proj.deepnet.caffenet_<TAB-COMPLETION>
    browser.auto.k8.anunez.proj.deepnet.caffenet_ANfs_performance_HDF
    browser.auto.k8.anunez.proj.deepnet.caffenet_BGfs_performance_HDF

    >>> browser.auto.k8.anunez.proj.deepnet.caffenet_BGfs_performance_HDF
    <h5py-like-group @anunez_raid bucket: caffenet_BGfs_performance.hdf (6 keys)>

    >>> # We can also explore the contents of the HDF-like object
    >>> browser.k8.anunez.proj.deepnet.caffenet_BGfs_performance_HDF.<TAB-COMPLETION>
    browser.auto.k8.anunez.proj.deepnet.caffenet_BGfs_performance_HDF.caffenet_fc6
    browser.auto.k8.anunez.proj.deepnet.caffenet_BGfs_performance_HDF.caffenet_fc7
    browser.auto.k8.anunez.proj.deepnet.caffenet_BGfs_performance_HDF.caffenet_fc8

    >>> # let's look at one
    >>> browser.auto.k8.anunez.proj.deepnet.caffenet_BGfs_performance_HDF.caffenet_fc8
    <h5py-like-dataset @anunez_raid bucket: caffenet_conv3 [shape=(73221)]>

    >>> # we can download the data as an array
    >>> arr = browser.auto.k8.anunez.proj.deepnet.caffenet_BGfs_performance_HDF.caffenet_fc8.load()
    >>> arr.shape
    (73221,)

    >>> # we can also download the object. useful when no class for object exists
    >>> browser.auto.k8.anunez.proj.deepnet.caffenet_BGfs_performance_HDF.caffenet_fc8()
    s3.Object(bucket_name='anunez_raid', key='auto/k8/anunez/proj/deepnet/caffenet_BGfs_performance.hdf/caffenet_fc8')
    """
    from .interfaces import DefaultInterface
    from .browser import S3Directory


    if (ACCESS_KEY is False) and (SECRET_KEY is False):
        from .utils import get_keys
        ACCESS_KEY, SECRET_KEY = get_keys()

    interface = DefaultInterface(bucket_name,
                                 ACCESS_KEY,
                                 SECRET_KEY,
                                 endpoint_url,
                                 verbose=False)

    return S3Directory('/', interface=interface)

__all__ = ['get_interface', 'get_browser', 'interfaces', 'browser']
