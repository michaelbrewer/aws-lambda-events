import pathlib
import setuptools

HERE = pathlib.Path(__file__).parent.parent
README = (HERE / "README.md").read_text()

setuptools.setup(
    name="aws-lambda-publish-shared-event",
    version="0.1.0",
    entry_points={
        "console_scripts": ["publish-shared-event=aws_lambda_publish_shared_event.__main__:main"],
    },
    author="Michael Brewer",
    license="MIT",
    description="Cli to publish shareable lambda test events.",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["aws_lambda_publish_shared_event"],
    install_requires=[
        "setuptools",
        "boto3 >= 1.21.23",
        "botocore >= 1.24.23",
        "pick >= 1.2.0",
    ],
    python_requires=">=3.7",
    include_package_data=True,
)
