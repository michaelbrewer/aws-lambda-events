import pathlib

import setuptools

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setuptools.setup(
    name="aws-lambda-publish-shared-event",
    version="0.17.0",
    entry_points={
        "console_scripts": [
            "publish-shared-event=aws_lambda_publish_shared_event.__main__:main",
            "generate-test-event=aws_lambda_publish_shared_event.generate_test_event.__main__:main",
        ],
    },
    author="Michael Brewer",
    license="MIT",
    url="https://lambda.101i.de/",
    description="Cli to publish shareable Lambda test events.",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["aws_lambda_publish_shared_event",  "aws_lambda_publish_shared_event.generate_test_event"],
    install_requires=[
        "boto3 >= 1.24.31",
        "botocore >= 1.27.31",
        "pick >= 1.4.0",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    project_urls={
        "GitHub": "https://github.com/michaelbrewer/aws-lambda-events",
        "Documentation": "https://lambda.101i.de/",
    },
)
