from setuptools import setup, find_packages

setup(
    name='rag_project',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'', 'src'},
    install_requires=[
        'transformers',
        'torch',
        'PyPDF2',
        'python-docx',
        'faiss-cpu',
    ],
)