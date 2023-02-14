<template>
	<view>
		<text>长连接数据：{{Message.info}}</text>
	</view>
</template>
<script>
import io from '@/flower/js_sdk/hyoga-uni-socket_io/uni-socket.io.js';
export default {
	data() {
		return {
			Message:{}，
			state：null,
			user:{
				id:'1111111',
				type:1
			}
		};
	},
	methods: {
		import io from '@/flower/js_sdk/hyoga-uni-socket_io/uni-socket.io.js';
		
		const socket = io('your websocket path', {
		  query: {},
		  transports: [ 'websocket', 'polling' ],
		  timeout: 5000,
		});
		
		socket.on('connect', () => {
		  // ws连接已建立，此时可以进行socket.io的事件监听或者数据发送操作
		  console.log('ws 已连接');
		  // socket.io 唯一连接id，可以监控这个id实现点对点通讯
		  const { id } = socket;
		  socket.on(id, (message) => {
		    // 收到服务器推送的消息，可以跟进自身业务进行操作
		    console.log('ws 收到服务器消息：', message);
		  });
		  // 主动向服务器发送数据
		  socket.emit('send_data', {
		    time: +new Date(),
		  });
		});
		
		socket.on('error', (msg: any) => {
		  console.log('ws error', msg);
		});
	}
}
</script>