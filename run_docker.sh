nvidia-docker run -it \
	-u 0:1017 \
	-e DISPLAY=$DISPLAY \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-v /home1/Users/sofie/:/root/workspace \
	-v /home1/Users/nishi/develop/:/root/develop \
	--name nishizaki_012 \
	-p 4268:5901 \
	solize:test_012

# �pport : 4250-4279
#  ����  4250-4252
#  �X�{  4256-4258
#  �O��  4265-4267
#  free  4268-4279
