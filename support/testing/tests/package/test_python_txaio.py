from tests.package.test_python import TestPythonPackageBase


class TestPythonPy3Txaio(TestPythonPackageBase):
    __test__ = True
    config = TestPythonPackageBase.config + \
        """
        BR2_PACKAGE_PYTHON3=y
        BR2_PACKAGE_PYTHON_TXAIO=y
        BR2_PACKAGE_PYTHON_TWISTED=y
        """
    sample_scripts = ["tests/package/sample_python_txaio_asyncio.py", "tests/package/sample_python_txaio_twisted.py"]
