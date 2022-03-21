import setuptools

setuptools.setup(
    name="aws-lambda-publish-shared-event",
    version="1.0",
    entry_points={
        "console_scripts": ["publish-shared-event=main:main"],
    },
    author="Michael Brewer",
    description="Cli to publish shareable lambda test events.",
    packages=["src"],
    install_requires=[
        "setuptools",
        "boto3 >= 1.21.23",
        "pick >= 1.2.0",
    ],
    python_requires=">=3.7",
    include_package_data=True,
)
