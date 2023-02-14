<template>
	<view>
		<view style="position: fixed;height: 1540rpx;">
			<image src="../../img/main/back.png" mode=""style="position: absolute;height: 1540rpx;width: 750rpx;z-index: 1;"></image>
		</view>
		<view style="width: 100%;height: 150px;position: fixed;bottom: 320px;<!-- background-color: #ff0000; -->opacity:0.5;">
			<navigator url="../../pages/index/loding?id=1"><image src="../../img/main/tree.png" mode=""style="position: absolute;z-index: 4;width: 90PX;height: 90PX;left: 20px;bottom: 10px;"></image></navigator>
			<navigator url="../../pages/index/loding?id=2"><image src="../../img/main/history.png" mode=""style="position: absolute;z-index: 4;width: 90PX;height: 90PX;left: 150px;bottom: 10px;"></image></navigator>
			<navigator url="../../pages/index/loding?id=3"><image src="../../img/main/stor.png" mode=""style="position: absolute;z-index: 4;width: 90PX;height: 90PX;right: 10px;bottom: 10px;"></image></navigator>
		</view>
		
		<view style="width: 100%;height: 330px;position: fixed;z-index: 0;bottom: -30px;<!-- background-color: #007AFF; -->opacity:0.5;">
			<swiper indicator-dots autoplay circular interval='3000' duration='1500' indicator-color="#2b2b00" indicator-active-color="#24aa2d" style="width: 100%;height: 300px;">
				<swiper-item>
					<image src="../../img/main/pic.png"style="width: 100%;height: 284px;bottom: -17px;"></image>
				</swiper-item>
				<swiper-item>
					<image src="../../img/main/lily.png"style="width: 100%;height: 300px;bottom: 0px;"></image>
				</swiper-item>
				<swiper-item>
					<image src="../../img/main/sunflower.png"style="width: 100%;height: 300px;bottom: 0px;"></image>
				</swiper-item>
			</swiper>
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
			
			
		}
	}
</script>

<style>
	#全局样式取消滚动条
	::-webkit-scrollbar{
	
	  display: none;
	
	}

</style>
