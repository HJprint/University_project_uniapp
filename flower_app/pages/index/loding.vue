<template>
	<view>
		<image src="../../img/logo/laoding.gif" mode="" style="background-color: #50d375;width: 100%;position: fixed;height: 1540rpx;"></image>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
		},
		onLoad: function (option) { //option为object类型，会序列化上个页面传递的参数
			        console.log(option.id); //打印出上个页面传递的参数。
			        
					var a = option.id
					if (a==1){//跳转我的种植界面
						setTimeout((a)=>{
							uni.navigateTo({
								url:"../../pages/index/myflower"
								
							})
						},2500)
					}
					if (a==2){//跳转历史界面
						setTimeout((a)=>{
							uni.navigateTo({
								url:"../../pages/index/history"
								
							})
						},2500)
					}
					if (a==3){//跳转商店界面
						setTimeout((a)=>{
							uni.navigateTo({
								url:"../../pages/index/stor"
								
							})
						},2500)
					}
					if (a==4){//跳转商店界面
						setTimeout((a)=>{
							uni.navigateTo({
								url:"../../pages/index/main"
								
							})
						},2500)
					}
					
				}
	}
</script>

<style>

</style>
