import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aniposelib",
    version="0.4.3",
    author="Pierre Karashchuk",
    author_email="krchtchk@gmail.com",
    description="An easy-to-use library for calibrating cameras in python, made for Anipose",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lambdaloop/aniposelib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Image Recognition"
    ],
    dependency_links=[
        'https://storage.googleapis.com/jax-releases/jax_cuda_releases.html'
    ],
    install_requires=[
        'opencv-contrib-python',
        'numba', 'pandas',
        'numpy', 'scipy', 'toml', 'tqdm',
        'jax'
    ],
    extras_require={
        'full':  ["checkerboard"]
    }
)
