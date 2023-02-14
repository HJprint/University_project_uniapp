<template>
	<button type="default" @click="tcp_tx2('3')" >通过navigator组件跳转到about页面</button>
</template>

<script>
	import socket from '../../socketio.js'
	export default {
		data() {
			return {
				er_wei_:0,		// 确保websocket是打开状态
			}
		},
		methods: {
			//接收数据
			tcp_tx:function(contorl){
				
				},
			//发送数据
			tcp_tx2:function(contorl){
				uni.request({
					url:'http://x3q3086476.51vip.biz',
					//url:'http://103.46.128.21:18014/',
					data: {
							age: 18,
							text: contorl//发送的变量
						},
					
					method:"POST",
					success: function(){
						console.log(contorl)
					}
				})
			}
		},
		}
</script>

<style>
	
</style>
