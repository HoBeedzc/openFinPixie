import os

from .version import __version__, digital_version

package_path = os.path.dirname(__file__)


def _welcome():
    print('+---------------------------------------+')
    print('|      open Fund Reminder Toolkit       |')
    print('|      ^^^^^^^^^^^^^^^^^^^^^^^^^^       |')
    print('|          author: Hobee Liu            |')
    print('+--------------------------------------+')
    print(
        'NOTICE: This software is licensed under the GNU General Public\n'
        'License v3.0 and SHALL NOT be used for commercial purpose. All\n'
        'rights reserved to Hobee Liu. Please contact me if the project\n'
        'has any potential infringement risks.',
    )


_welcome()


__all__ = ['__version__', 'digital_version', 'package_path']