<template>
	<view id='all'>
		<view >
			<image id='login_back' src="../../img/login/login_back.png" mode=""></image>
		</view>
		<view class="lolin" style="position: fixed;z-index: 2;height: 300px;width:100%;bottom: 180px;<!-- background-color: #007AFF; -->opacity:0.5;">
			<view class="zhanghao" style="position: absolute;z-index: 3;height: 200px;width: 100%;bottom: 100px;<!-- background-color: #000000; -->opacity:0.5;">
				<image src="../../img/login/zhang.png" mode=""style="position: absolute;z-index: 4;width: 70PX;height: 70PX;left: 2px;bottom: 100px;"></image>
				<image src="../../img/login/shuru.png" mode=""style="position: absolute;z-index: 4;height: 80px;width: 310px;bottom: 80px;left: 60px;"></image>
				<input type="text" placeholder="请输入账号"  style="position: absolute;z-index: 4;border-bottom:3px #333333 solid ;width:254px;bottom: 112px;left: 84px;"/>
				<image src="../../img/login/login_pass.png" style="position: absolute;z-index: 4;width: 74PX;height: 74PX;left: -2px;bottom: 10px;" mode=""></image>
				<image src="../../img/login/shuru.png" mode=""style="position: absolute;z-index: 4;height: 80px;width: 310px;bottom: 0px;left: 60px;"></image>
				<input type="password" placeholder="请输入密码" style="position: absolute;z-index: 4;border-bottom:3px #333333 solid ;width:254px;bottom: 34px;left: 84px;"/>
			</view>
			<view class="pass" style="position: absolute;z-index: 4;height: 100px;width: 100%;bottom: 0px;<!-- background-color: #aa0002; -->opacity:0.5;">
				<navigator url="../../pages/index/loding?id=4"><image @click="chang_tcp()" src="../../img/login/login_sing.png" style="position: absolute;z-index: 4;width: 84PX;height: 84PX;right: 70px;bottom: 10px;"></image></navigator>
				<navigator url="../../pages/index/index"><image src="../../img/login/login_zhuce.png"style="position: absolute;z-index: 4;width: 70PX;height: 70PX;left: 70px;bottom: 10px;"></image></navigator>
			</view>
		</view>
		<view class="qqwx"style="position: fixed;z-index: 4;height: 50px;width: 100%;bottom: 70px;<!-- background-color: #aa0002; -->opacity:0.5;">
			<image src="../../img/login/login_qq.png" style="position: absolute;z-index: 4;width: 36PX;height: 36PX;right: 120px;bottom: 0px;" mode=""></image>
			<image src="../../img/login/login_wx.png" style="position: absolute;z-index: 4;width: 36PX;height: 36PX;left: 120px;bottom: 0px;" mode=""></image>
		</view>
	</view>
</template>

<script>
	
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			gotomain:function(){
				 uni.navigateTo({
				            url:"../../pages/index/main"})
			},
			//建立长通信
			chang_tcp:function(){
				uni.connectSocket({
				    url: 'http://x3q3086476.51vip.biz',
				    data() {
				        return {
				            x: '',
				            y: ''
				        };
				    },
				    header: {
				        'content-type': 'application/json'
				    },
				    protocols: ['protocol1'],
				    method: 'GET'
				});
			},
		}
	}
</script>


<style>
	#全局样式取消滚动条
	::-webkit-scrollbar{
	
	  display: none;
	
	}
	#all{
		position: fixed;height: 1540rpx;
	}
	#login_back{
		position: absolute;height: 1540rpx;
		width: 750rpx;
		z-index: 1;
		
	}
</style>
