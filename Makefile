DEV_IMAGE := registry.cn-beijing.aliyuncs.com/wa/dev:tf-py3

dev:
	pipenv shell
# dev:
# 	docker run --rm -it \
# 	 --name tf-learning \
# 	 -v `pwd`:/opt/tf \
# 	 -w /opt/tf \
# 	 ${DEV_IMAGE} bash

build:
	pipenv install --ignore-pipfile
