<template>
	<view v-if="type === 'A'">
		<!-- 背景 -->
		<view style="position: fixed;height: 1540rpx;">
			<image src="../../img/stor/bac.png" mode=""style="position: absolute;height: 1540rpx;width: 750rpx;z-index: 1;"></image>
		</view>
		<!-- 头部 -->
		<view class="" style="width: 100%;height: 137px;position: fixed;z-index: 2;<!-- background-color: #007AFF; -->opacity:0.5;">
			<!-- 返回 -->
			<navigator url="../../pages/index/main"><image src="../../img/stor/return.png" mode=""style="width: 80rpx;height: 80rpx;position: absolute;z-index: 3; left: 26px;top:41px;"></image></navigator>
			<!-- 标题栏 -->
			<view class="" style="width: 100%;height: 45px;position: absolute;z-index: 4;bottom: 0px;<!-- background-color: #ff103c; -->opacity:0.5;">
				<image @click="qie_huan('A')"src="../../img/stor/head1.png" mode=""style="position: absolute;width: 90px;height: 22px;left: 45px;bottom: 10px;z-index: 5;"></image>
				<image @click="qie_huan('B')"src="../../img/stor/head2_p.png" mode=""style="position: absolute;width: 70px;height: 15px;right: 55px;bottom: 11px;z-index: 5;"></image>
			</view>
			<!-- 能量豆 -->
			<view style="width: 90px;height: 30px;position: fixed;top:43px;right: 15px;z-index: 2;<!-- background-color: #007AFF; -->opacity:0.5;">
				<text style="position: absolute;top:2px;left: 35px;z-index: 2;color: #4CD964;">{{money}}</text>
			</view>
		</view>
		<!-- 身体 -->
		<view class="" style="position: fixed;z-index: 2;width: 100%;height: 528px;bottom: 70px;<!-- background-color: #ce090d; -->opacity:0.5;">
			<image src="../../img/stor/flower1.png" mode="" style="position: absolute;width: 150px;height: 200px;left: 20px;top: 20px;z-index: 5;"></image>
			<image src="../../img/stor/flower2.png" mode="" style="position: absolute;width: 150px;height: 200px;right: 20px;top: 20px;z-index: 5;"></image>
			<image src="../../img/stor/flower3.png" mode="" style="position: absolute;width: 150px;height: 200px;left: 20px;bottom: 50px;z-index: 5;"></image>
			<image src="../../img/stor/flower4.png" mode="" style="position: absolute;width: 150px;height: 200px;right: 20px;bottom: 50px;z-index: 5;"></image>
			
			<navigator url=""><image @click="yu_lan(1,200)" src="../../img/stor/200.png" mode="" style="position: absolute;width: 80px;height: 30px;left: 55px;top: 225px;z-index: 5;"></image></navigator>
			<navigator url=""><image @click="yu_lan(2,300)"src="../../img/stor/300.png" mode="" style="position: absolute;width: 80px;height: 30px;right: 55px;top: 225px;z-index: 5;"></image></navigator>
			<navigator url=""><image @click="yu_lan(3,400)"src="../../img/stor/400.png" mode="" style="position: absolute;width: 80px;height: 30px;left: 55px;bottom: 15px;z-index: 5;"></image></navigator>
			<navigator url=""><image @click="yu_lan(4,450)"src="../../img/stor/450.png" mode="" style="position: absolute;width: 80px;height: 30px;right: 55px;bottom: 15px;z-index: 5;"></image></navigator>
			
		</view>
		<!-- 底部 -->
		<view DDclass="" style="width: 100%;height: 65px;bottom: 0px;position: fixed;z-index: 2;<!-- background-color: #007AFF; -->opacity:0.5;">
			<navigator url=""><image src="../../img/stor/xia.png" mode="" style="position: absolute;width: 80px;height: 30px;left: 34px;bottom: 20px;z-index: 5;"></image></navigator>
			<navigator url=""><image src="../../img/stor/ye.png" mode="" style="position: absolute;width: 80px;height: 30px;left: 145px;bottom: 20px;z-index: 5;"></image></navigator>
			<navigator url=""><image src="../../img/stor/shang.png" mode="" style="position: absolute;width: 80px;height: 30px;right: 30px;bottom: 20px;z-index: 5;"></image></navigator>
		</view>
		<!-- 弹窗 -->
		<view v-if="cuo_wu===123">
			<!-- 背景 -->
			<view style="position: fixed;height: 1540rpx;top:0px;z-index: 10;">
				<image src="../../img/stor/bac_yu.png" mode=""style="position: fixed;height: 1540rpx;width: 750rpx;z-index: 10;opacity:0.6;"></image>
			</view>
			<image src="../../img/stor/shibai.png" mode="" style="position: fixed;height: 280rpx;width: 570rpx;z-index: 10;top: 300px;left: 50px;"></image>
			<image @click="yu_lan(0)" src="../../img/stor/guanbi2.png" style="position: fixed;width: 60px;height: 25px;right: 150px;top: 400px;z-index: 11;"></image>
		</view>
		<view v-if="road===1">
			<!-- 背景 -->
			<view style="position: fixed;height: 1540rpx;top:0px;z-index: 10;">
				<image src="../../img/stor/bac_yu.png" mode=""style="position: fixed;height: 1540rpx;width: 750rpx;z-index: 10;opacity:0.6;"></image>
			</view>
			<!-- 预览 -->
			<view style="position: fixed;height: 900rpx;width: 300px;top:150px;left: 35px;z-index: 10;background-color: #00aa7f;opacity:1;">
				<image src="../../img/stor/goumai.png" style="position: absolute;width: 220px;height: 60px;left: 40px;top: 250px;z-index: 12;border-radius:10px;"></image>
				<image src="../../img/stor/flower1.png" style="position: absolute;width: 150px;height: 200px;left: 75px;top: 20px;z-index: 11;"></image>
				<navigator url="../../pages/index/myflower?id=1"><image src="../../img/stor/qianwang.png" style="position: absolute;width: 100px;height: 40px;left: 30px;bottom: 40px;z-index: 11;"></image></navigator>
				<navigator url=""><image @click="yu_lan(0)" src="../../img/stor/guanbi.png" style="position: absolute;width: 100px;height: 40px;right: 30px;bottom: 40px;z-index: 11;"></image></navigator>
				
			</view>
		</view>
		<view v-if="road===2">
			<!-- 背景 -->
			<view style="position: fixed;height: 1540rpx;top:0px;z-index: 10;">
				<image src="../../img/stor/bac_yu.png" mode=""style="position: fixed;height: 1540rpx;width: 750rpx;z-index: 10;opacity:0.6;"></image>
			</view>
			<!-- 预览 -->
			<view style="position: fixed;height: 900rpx;width: 300px;top:150px;left: 35px;z-index: 10;background-color: #00aa7f;opacity:1;">
				<image src="../../img/stor/goumai.png" style="position: absolute;width: 220px;height: 60px;left: 40px;top: 250px;z-index: 12;"></image>
				<image src="../../img/stor/flower2.png" style="position: absolute;width: 150px;height: 200px;left: 75px;top: 20px;z-index: 11;"></image>
				<navigator url="../../pages/index/myflower?id=1"><image src="../../img/stor/qianwang.png" style="position: absolute;width: 100px;height: 40px;left: 30px;bottom: 40px;z-index: 11;"></image></navigator>
				<navigator url=""><image @click="yu_lan(0)" src="../../img/stor/guanbi.png" style="position: absolute;width: 100px;height: 40px;right: 30px;bottom: 40px;z-index: 11;"></image></navigator>
				
			</view>
		</view>
		<view v-if="road===3">
			<!-- 背景 -->
			<view style="position: fixed;height: 1540rpx;top:0px;z-index: 10;">
				<image src="../../img/stor/bac_yu.png" mode=""style="position: fixed;height: 1540rpx;width: 750rpx;z-index: 10;opacity:0.6;"></image>
			</view>
			<!-- 预览 -->
			<view style="position: fixed;height: 900rpx;width: 300px;top:150px;left: 35px;z-index: 10;background-color: #00aa7f;opacity:1;">
				<image src="../../img/stor/goumai.png" style="position: absolute;width: 220px;height: 60px;left: 40px;top: 250px;z-index: 12;"></image>
				<image src="../../img/stor/flower3.png" style="position: absolute;width: 150px;height: 200px;left: 75px;top: 20px;z-index: 11;"></image>
				<!-- <navigator url="../../pages/index/myflower?id=1"><image src="../../img/stor/qianwang.png" style="position: absolute;width: 100px;height: 40px;left: 30px;bottom: 40px;z-index: 11;"></image></navigator> -->
				<navigator url="../../pages/index/myflower?id=1"><image src="../../img/stor/qianwang.png" style="position: absolute;width: 100px;height: 40px;left: 30px;bottom: 40px;z-index: 11;"></image></navigator>
				<navigator url=""><image @click="yu_lan(0)" src="../../img/stor/guanbi.png" style="position: absolute;width: 100px;height: 40px;right: 30px;bottom: 40px;z-index: 11;"></image></navigator>
				
			</view>
		</view>
		<view v-if="road===4">
			<!-- 背景 -->
			<view style="position: fixed;height: 1540rpx;top:0px;z-index: 10;">
				<image src="../../img/stor/bac_yu.png" mode=""style="position: fixed;height: 1540rpx;width: 750rpx;z-index: 10;opacity:0.6;"></image>
			</view>
			<!-- 预览 -->
			<view style="position: fixed;height: 900rpx;width: 300px;top:150px;left: 35px;z-index: 10;background-color: #00aa7f;opacity:1;">
				<image src="../../img/stor/goumai.png" style="position: absolute;width: 220px;height: 60px;left: 40px;top: 250px;z-index: 12;"></image>
				<image src="../../img/stor/flower4.png" style="position: absolute;width: 150px;height: 200px;left: 75px;top: 20px;z-index: 11;"></image>
				<navigator url="../../pages/index/myflower?id=1"><image src="../../img/stor/qianwang.png" style="position: absolute;width: 100px;height: 40px;left: 30px;bottom: 40px;z-index: 11;"></image></navigator>
				<navigator url=""><image @click="yu_lan(0)" src="../../img/stor/guanbi.png" style="position: absolute;width: 100px;height: 40px;right: 30px;bottom: 40px;z-index: 11;"></image></navigator>
				
			</view>
		</view>
		
	</view>
	<view v-else-if="type === 'B'">
		<!-- 背景 -->
		<view style="position: fixed;height: 1540rpx;">
			<image src="../../img/stor/bac2.png" mode=""style="position: absolute;height: 1540rpx;width: 750rpx;z-index: 1;"></image>
		</view>
		<!-- 头部 -->
		<view class="" style="width: 100%;height: 137px;position: fixed;z-index: 2;<!-- background-color: #007AFF; -->opacity:0.5;">
			<!-- 返回 -->
			<navigator url="../../pages/index/main"><image src="../../img/stor/return.png" mode=""style="width: 80rpx;height: 80rpx;position: absolute;z-index: 3; left: 26px;top:41px;"></image></navigator>
			<!-- 标题栏 -->
			<view class="" style="width: 100%;height: 45px;position: absolute;z-index: 4;bottom: 0px;<!-- background-color: #ff103c; -->opacity:0.5;">
				<image @click="qie_huan('A')"src="../../img/stor/head1_p.png" mode=""style="position: absolute;width: 70px;height: 15px;left: 57px;bottom: 11px;z-index: 5;"></image>
				<image @click="qie_huan('B')"src="../../img/stor/head2.png" mode=""style="position: absolute;width: 95px;height: 22px;right: 45px;bottom: 11px;z-index: 5;"></image>
			</view>
			<!-- 能量豆 -->
			<view class="">
				
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				type:'A',
				money:800,
				road:0,
				cuo_wu:0,
			}
		},
		methods: {
			//导航栏切换
			qie_huan:function(qie){
				this.type=qie
			},
			//扣钱
			kou_qian:function(qian){
				if (this.money>=qian){
					
					this.cuo_wu=0
				}
				else{
					this.cuo_wu=123
				}
			},
			//预览
			yu_lan:function(pic,qian){
				
				if (this.money>=qian){
					this.money=this.money-qian
					this.cuo_wu=0
					this.road=pic
				}
				else{
					this.cuo_wu=123
				}
				if (pic==0){
					this.cuo_wu=0
					this.road=pic
				}
			}
			
		}
	}
</script>

<style>

</style>
