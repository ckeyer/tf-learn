DEV_IMAGE := registry.cn-beijing.aliyuncs.com/wa/dev:tf-py3

dev:
	docker run --rm -it \
	 --name tf-learning \
	 -v `pwd`:/opt/tf \
	 -w /opt/tf \
	 ${DEV_IMAGE} bash
