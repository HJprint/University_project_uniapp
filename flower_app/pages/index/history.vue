<template>
	<view v-if="type === 'A'">
		<!-- 背景 -->
		<view style="position: fixed;height: 1540rpx;">
			<image src="../../img/history/bac.png" mode=""style="position: absolute;height: 1540rpx;width: 750rpx;z-index: 1;"></image>
		</view>
		<!-- 头部 -->
		<view class="" style="width: 100%;height: 137px;position: fixed;z-index: 2;<!-- background-color: #007AFF; -->opacity:0.5;">
			<!-- 返回 -->
			<navigator url="../../pages/index/main"><image src="../../img/myflower/return.png" mode=""style="width: 80rpx;height: 80rpx;position: absolute;z-index: 3; left: 25px;top:40px;"></image></navigator>
			<!-- 标题栏 -->
			<view class="" style="width: 100%;height: 45px;position: absolute;z-index: 4;bottom: 0px;<!-- background-color: #ff103c; -->opacity:0.5;">
				<image @click="qie_huan('A')" src="../../img/history/head1.png" mode=""style="position: absolute;width: 95px;height: 26px;left: 25px;bottom: 8px;z-index: 5;"></image>
				<image @click="qie_huan('B')" src="../../img/history/head3_p.png" mode=""style="position: absolute;width: 70px;height: 18px;left: 156px;bottom: 13px;z-index: 5;"></image>
				<image @click="tan_chaung(1)" src="../../img/history/head2_p.png" mode=""style="position: absolute;width: 70px;height: 15px;right: 31px;bottom: 14px;z-index: 5;"></image>
			</view>
		</view>
		<!-- 视屏流 -->
		<view class="">
			<view v-if="an===1">
				<image @click="an_niu(2)"src="../../img/history/shi_.png" style="position: fixed;width: 40px;height: 40px;right: 30px;top: 170px;z-index: 5;"></image>
				<image @click="an_niu(1)"src="../../img/history/ka_p.png" style="position: fixed;width: 40px;height: 40px;left: 30px;top: 170px;z-index: 5;"></image>
			</view>
			<view v-else-if="an===2">
				<image @click="an_niu(2)"src="../../img/history/shi_p.png" style="position: fixed;width: 40px;height: 40px;right: 30px;top: 170px;z-index: 5;"></image>
				<image @click="an_niu(1)"src="../../img/history/ka_.png" style="position: fixed;width: 40px;height: 40px;left: 30px;top: 170px;z-index: 5;"></image>
			</view>
		</view>
		<view class=""style="width: 100px;height: 100px;position: fixed;z-index: 2;top: 225px;left: 30px;<!-- background-color: #007AFF; -->opacity:0.5;">
			<view v-if="shi_ ===0">
				<image @click="jie_suo(2)" src="../../img/history/action.png" alt="" style="width: 302px;height: 270px;position: absolute;z-index: 2;top: 0px;left: 0px;<!-- background-color: #007AFF;opacity:0.5; -->"></image>
			</view>
			<view v-else-if="shi_===1">
				<!-- <video src="../../img/history/hecheng.mp4" controls style="width: 302px;height: 270px;position: absolute;z-index: 3;top: 0px;left: 0px;"></video> -->
				<image src="../../img/history/hecheng.gif" style="width: 302px;height: 270px;position: absolute;z-index: 3;top: 0px;left: 0px;"></image>
			</view>
			<view v-else-if="shi_===2">
				<!-- <video src="../../img/history/hecheng.mp4" controls style="width: 302px;height: 270px;position: absolute;z-index: 3;top: 0px;left: 0px;"></video> -->
				<image src="../../img/history/hecheng2.gif" style="width: 302px;height: 270px;position: absolute;z-index: 3;top: 0px;left: 0px;"></image>
			</view>
			
		</view>
		<!-- 十天 -->
		<view class="" style="width: 100%;height: 230px;position: fixed;z-index: 2;bottom: 0px;left: 0px;<!-- background-color: #007AFF;opacity:0.5; -->">
			<image src="../../img/history/1.png" mode="" style="width: 60px;height: 60px;position: absolute;z-index: 2;top: 30px;left: 10px;<!-- background-color: #007AFF;opacity:0.5; -->"></image>
			<image src="../../img/history/2.png" mode="" style="width: 60px;height: 60px;position: absolute;z-index: 2;top: 30px;left: 80px;<!-- background-color: #007AFF;opacity:0.5; -->"></image>
			<image src="../../img/history/3.png" mode="" style="width: 60px;height: 60px;position: absolute;z-index: 2;top: 30px;;left: 150px;<!-- background-color: #007AFF;opacity:0.5; -->"></image>
			<image src="../../img/history/4.png" mode="" style="width: 60px;height: 60px;position: absolute;z-index: 2;top: 30px;;left: 220px;<!-- background-color: #007AFF;opacity:0.5; -->"></image>
			<image src="../../img/history/5.png" mode="" style="width: 60px;height: 60px;position: absolute;z-index: 2;top: 30px;;left: 290px;<!-- background-color: #007AFF;opacity:0.5; -->"></image>
			<image src="../../img/history/6.png" mode="" style="width: 60px;height: 60px;position: absolute;z-index: 2;bottom: 40px;left: 10px;<!-- background-color: #007AFF;opacity:0.5; -->"></image>
			<image src="../../img/history/7.png" mode="" style="width: 60px;height: 60px;position: absolute;z-index: 2;bottom: 40px;left: 80px;<!-- background-color: #007AFF;opacity:0.5; -->"></image>
			<image src="../../img/history/8.png" mode="" style="width: 60px;height: 60px;position: absolute;z-index: 2;bottom: 40px;left: 150px;<!-- background-color: #007AFF;opacity:0.5; -->"></image>
			<image src="../../img/history/9.png" mode="" style="width: 60px;height: 60px;position: absolute;z-index: 2;bottom: 40px;left: 220px;<!-- background-color: #007AFF;opacity:0.5; -->"></image>
			<image src="../../img/history/10.png" mode="" style="width: 60px;height: 60px;position: absolute;z-index: 2;bottom: 40px;left: 290px;<!-- background-color: #007AFF;opacity:0.5; -->"></image>
		</view>
		<view v-if="tan === 1">
			<image src="../../img/myflower/weikaif.png" style="position: fixed;width: 280px;height: 80px;right: 40px;top: 140px;z-index: 7;"></image>
		</view>
		<view v-else-if="tan === 2">
			<image src="../../img/myflower/jiesuo.png" style="position: fixed;width: 280px;height: 80px;right: 40px;top: 140px;z-index: 7;"></image>
		</view>
	</view>
	<view v-else-if="type === 'B'">
		<!-- 背景 -->
		<view style="position: fixed;height: 1540rpx;">
			<image src="../../img/history/bac2.png" mode=""style="position: absolute;height: 1540rpx;width: 750rpx;z-index: 1;"></image>
		</view>
		<!-- 头部 -->
		<view class="" style="width: 100%;height: 137px;position: fixed;z-index: 2;<!-- background-color: #007AFF; -->opacity:0.5;">
			<!-- 返回 -->
			<navigator url="../../pages/index/main"><image src="../../img/myflower/return.png" mode=""style="width: 80rpx;height: 80rpx;position: absolute;z-index: 3; left: 25px;top:40px;"></image></navigator>
			<!-- 标题栏 -->
			<view class="" style="width: 100%;height: 45px;position: absolute;z-index: 4;bottom: 0px;<!-- background-color: #ff103c; -->opacity:0.5;">
				<image @click="qie_huan('A')" src="../../img/history/head1_p.png" mode=""style="position: absolute;width: 70px;height: 15px;left: 37px;bottom: 14px;z-index: 5;"></image>
				<image @click="qie_huan('B')" src="../../img/history/head2.png" mode=""style="position: absolute;width: 95px;height: 26px;left: 145px;bottom: 8px;z-index: 5;"></image>
				<image @click="tan_chaung(1)" src="../../img/history/head2_p.png" mode=""style="position: absolute;width: 72px;height: 15px;right: 31px;bottom: 14px;z-index: 5;"></image>
			</view>
		</view>
		<view v-if="tan === 1">
			<image src="../../img/myflower/weikaif.png" style="position: fixed;width: 280px;height: 80px;right: 40px;top: 140px;z-index: 7;"></image>
		</view>
	</view>
	<view v-else-if="type === 'C'">
		<!-- 背景 -->
		<view style="position: fixed;height: 1540rpx;">
			<image src="../../img/history/bac3.png" mode=""style="position: absolute;height: 1540rpx;width: 750rpx;z-index: 1;"></image>
		</view>
		<!-- 头部 -->
		<view class="" style="width: 100%;height: 137px;position: fixed;z-index: 2;<!-- background-color: #007AFF; -->opacity:0.5;">
			<!-- 返回 -->
			<navigator url="../../pages/index/main"><image src="../../img/myflower/return.png" mode=""style="width: 80rpx;height: 80rpx;position: absolute;z-index: 3; left: 25px;top:40px;"></image></navigator>
			<!-- 标题栏 -->
			<view class="" style="width: 100%;height: 45px;position: absolute;z-index: 4;bottom: 0px;<!-- background-color: #ff103c; -->opacity:0.5;">
				<image @click="qie_huan('A')" src="../../img/history/head1_p.png" mode=""style="position: absolute;width: 70px;height: 18px;left: 38px;bottom: 12px;z-index: 5;"></image>
				<image @click="qie_huan('B')" src="../../img/history/head3_p.png" mode=""style="position: absolute;width: 70px;height: 18px;left: 154px;bottom: 12px;z-index: 5;"></image>
				<image @click="qie_huan('C')" src="../../img/history/head3.png" mode=""style="position: absolute;width: 95px;height: 26px;right: 25px;bottom: 8px;z-index: 5;"></image>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				type:'A',
				tan:0,
				shi_:0,
				an:1,
				
			}
		},
		methods: {
			//导航栏切换
			qie_huan:function(qie){
				this.type=qie
			},
			//弹窗
			tan_chaung:function(tan_data2){
				this.tan=tan_data2//先显示
				setTimeout((tan_data)=>{
					this.tan=0
				},1500)
			},
			//解锁
			jie_suo:function(tan_data){
				this.tan=tan_data//先显示
				setTimeout((tan_data)=>{
					this.tan=0
				},1500)
				if(this.an==1){
					this.shi_=1
				}
				if(this.an==2){
					this.shi_=2
				}
			},
			//按钮
			an_niu:function(an_data){
				this.an=an_data
			}
			
			
		}
	}
</script>

<style>

</style>
