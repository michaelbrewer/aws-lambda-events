import setuptools

setuptools.setup(
    name="aws-lambda-publish-shared-event",
    version="1.0",
    scripts=["./scripts/publish-shared-event"],
    author="Michael Brewer",
    description="Cli to publish shareable lambda test events.",
    packages=["src"],
    install_requires=[
        "setuptools",
        "boto3 >= 1.21.22",
        "pick >= 1.2.0",
    ],
    python_requires=">=3.7",
)
