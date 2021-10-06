from setuptools import setup, find_packages

setup(name='package', # 패키지명

version='0.0.1', #버전명

description='', #설명

author='smartwe', #제작자 이름

author_email='sparklingwee@gmail.com', #이메일

url='https://github.dev/smartwe/pypi', #홈페이지

license='MIT', #라이센스의 종류

py_modules=['package'], #패키지에 포함되는 모듈(이 레포의 경우 package.py)

python_requires='>=3', #파이썬 버전 제한

install_requires=[], #필요 패키지

packages=['package'] #패키지가 있는 폴더

)