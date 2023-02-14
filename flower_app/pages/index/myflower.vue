<template>
	<view v-if="type === 'A'">
		<!-- 背景 -->
		<view style="position: fixed;height: 1540rpx;">
			<image src="../../img/myflower/bac.png" mode=""style="position: absolute;height: 1540rpx;width: 750rpx;z-index: 1;"></image>
		</view>
		
		<!-- 头部 -->
		<view class="" style="width: 100%;height: 137px;position: fixed;z-index: 2;<!-- background-color: #007AFF; -->opacity:0.5;">
			<!-- 返回 -->
			<navigator url="../../pages/index/main"><image src="../../img/myflower/return.png" mode=""style="width: 80rpx;height: 80rpx;position: absolute;z-index: 3; left: 26px;top:39px;"></image></navigator>
			<!-- 标题栏 -->
			<view class="" style="width: 100%;height: 45px;position: absolute;z-index: 4;bottom: 0px;<!-- background-color: #ff103c; -->opacity:0.5;">
				<image @click="qie_huan('A')" src="../../img/myflower/myplant.png" mode=""style="position: absolute;width: 95px;height: 26px;left: 25px;bottom: 8px;z-index: 5;"></image>
				<navigator url=""><image @click="tan_chuang(5)" src="../../img/myflower/bao.png" mode=""style="position: absolute;width: 80px;height: 15px;left: 150px;bottom: 13px;z-index: 5;"></image></navigator>
				<!-- <image @click="qie_huan('C')" src="../../img/myflower/dianzhang_n.png" mode=""style="position: absolute;width: 70px;height: 15px;right: 31px;bottom: 14px;z-index: 5;"></image> -->
			</view>
			<!-- 头像 -->
			<view class=""style="position: fixed;width: 120px;height: 100px;right: 0px;top: 26px;z-index: 6;<!-- background-color: #007AFF; -->opacity:0.5;">
				<navigator url=""><image  @click="qie_huan('D')" src="../../img/myflower/tou.png" style="position: absolute;width: 50px;height: 50px;right: 36px;top: 10px;z-index: 6;"></image></navigator>
				<navigator url=""><image src="../../img/myflower/jia.png" style="position: absolute;width: 20px;height: 20px;right: 10px;bottom: 0px;z-index: 6;"></image></navigator>
				<image src="../../img/myflower/son.png" style="position: absolute;width: 20px;height: 20px;left: 10px;bottom: 0px;z-index: 6;"></image>
				<image src="../../img/myflower/kong.png" style="position: absolute;width: 20px;height: 20px;left: 36px;bottom: 0px;z-index: 6;"></image>
				<image src="../../img/myflower/kong.png" style="position: absolute;width: 20px;height: 20px;right: 36px;bottom: 0px;z-index: 6;"></image>
			</view>
		</view>
		<!-- 温度 -->
		<view class="" style="position: fixed;z-index: 2;width: 68%;height: 10px;right: 10px;top: 155px;">
			<progress :percent="p1" activeColor="#3dff57" stroke-width="15" show-info="True"/></view>
		<view class="" style="position: fixed;z-index: 2;width: 68%;height: 10px;right: 10px;top: 180px;">
			<progress :percent="p2" activeColor="#3dff57" stroke-width="15" show-info="True"/></view>
		<view class="" style="position: fixed;z-index: 2;width: 68%;height: 10px;right: 10px;top: 203px;">
			<progress :percent="p3" activeColor="#3dff57" stroke-width="15" show-info="True"/></view>
		<view class="" style="position: fixed;z-index: 2;width: 68%;height: 10px;right: 10px;top: 228px;">
			<progress :percent="p4" activeColor="#3dff57" stroke-width="15" show-info="True"/></view>
		<!-- 方框 -->
		<view class="" style="position: fixed;z-index: 2;width: 100%;height: 370px;bottom: 110px;<!-- background-color: #ce090d; -->opacity:0.5;">
			<!-- 视频流 -->
			<view v-if="tu === 0">
				<image src="../../img/myflower/meiyou.png" style="position: fixed;z-index: 3;width: 304px;height: 286px;bottom: 148px;left: 28px;"></image>
				<navigator url="../../pages/index/stor"><image src="../../img/myflower/goumai.png" style="position: fixed;z-index: 4;width: 160px;height: 70px;bottom: 220px;left: 105px;"></image></navigator>
				<navigator url=""><image src="../../img/myflower/goumai.png" style="position: fixed;z-index: 4;width: 160px;height: 70px;bottom: 220px;left: 105px;"></image></navigator>
			</view>
			<view v-else-if="tu === 1">
				<image src="../../img/myflower/shi.png" style="position: fixed;z-index: 3;width: 304px;height: 286px;bottom: 148px;left: 28px;"></image>
			</view>
			<!-- <navigator url=""><image @click="tcp_tx2('9')" src="../../img/myflower/katong.png" mode=""style="position: absolute;width: 80px;height: 30px;right: 25px;top: 5px;z-index: 5;"></image></navigator>
			<navigator url=""><image @click="tcp_tx2('a')" src="../../img/myflower/xianshi.png" mode=""style="position: absolute;width: 80px;height: 30px;left: 25px;top: 5px;z-index: 5;"></image></navigator> -->
			<navigator url=""><image @click="tcp_tx2('5')" src="../../img/myflower/s.png" mode=""style="position: absolute;width: 40px;height: 15px;left: 160px;top: 23px;z-index: 5;"></image></navigator>
			<navigator url=""><image @click="tcp_tx2('6')" src="../../img/myflower/x.png" mode=""style="position: absolute;width: 40px;height: 15px;left: 160px;bottom: 12px;z-index: 5;"></image></navigator>
			<navigator url=""><image @click="tcp_tx2('7')" src="../../img/myflower/z.png" mode=""style="position: absolute;width: 15px;height: 40px;left: 5px;bottom: 180px;z-index: 5;"></image></navigator>
			<navigator url=""><image @click="tcp_tx2('8')" src="../../img/myflower/y.png" mode=""style="position: absolute;width: 15px;height: 40px;right: 5px;bottom: 180px;z-index: 5;"></image></navigator>
		</view>
		<!-- 按钮 -->
		<view class="" style="position: fixed;z-index: 2;width: 100%;height: 110px;bottom: 0px;<!-- background-color: #78ffeb; -->opacity:0.5;">
			<navigator url=""><image @click="tcp_tx2('1',1,1)" src="../../img/myflower/sun.png" mode=""style="position: absolute;width: 70px;height: 90px;left: 20px;bottom: 15px;z-index: 5;"></image></navigator>
			<navigator url=""><image @click="tcp_tx2('2',2,2)" src="../../img/myflower/water.png" mode="" style="position: absolute;width: 70px;height: 90px;left: 105px;bottom: 15px;z-index: 5;"></image></navigator>
			<navigator url=""><image @click="tcp_tx2('3',3,3)" src="../../img/myflower/temptrul.png" mode="" style="position: absolute;width: 70px;height: 90px;right: 103px;bottom: 15px;z-index: 5;"></image></navigator>
			<navigator url=""><image @click="tcp_tx2('4',4)" src="../../img/myflower/zidong.png" mode="" style="position: absolute;width: 70px;height: 90px;right: 20px;bottom: 15px;z-index: 5;"></image></navigator>
			<view v-if="tan2===1">
				<image src="../../img/myflower/tan_guangzhao.png" style="position: fixed;width: 280px;height: 80px;right: 38px;top: 300px;z-index: 7;"></image>
			</view>
			<view v-else-if="tan2===2">
				<image src="../../img/myflower/tan_jiaoshui.png" style="position: fixed;width: 280px;height: 80px;right: 38px;top: 300px;z-index: 7;"></image>
			</view>
			<view v-else-if="tan2===3">
				<image src="../../img/myflower/tan_jiangwen.png" style="position: fixed;width: 280px;height: 80px;right: 38px;top: 300px;z-index: 7;"></image>
			</view>
		</view>
		<!-- 弹窗 -->
		<!-- <view v-if="tan === 1">
			<image src="../../img/myflower/b_guang.png" style="position: fixed;width: 280px;height: 80px;right: 40px;bottom: 350px;z-index: 7;"></image>
		</view>
		<view v-else-if="tan === 2">
			<image src="../../img/myflower/b_shui.png" style="position: fixed;width: 280px;height: 80px;right: 40px;bottom: 350px;z-index: 7;"></image>
		</view>
		<view v-else-if="tan === 3">
			<image src="../../img/myflower/b_wendu.png" style="position: fixed;width: 280px;height: 80px;right: 40px;bottom: 350px;z-index: 7;"></image>
		</view>
		<view v-else-if="tan === 4">
			<image src="../../img/myflower/b_zidong.png" style="position: fixed;width: 280px;height: 80px;right: 40px;bottom: 350px;z-index: 7;"></image>
		</view> -->
		<view v-if="tan === 5">
			<image src="../../img/myflower/weikaif.png" style="position: fixed;width: 280px;height: 80px;right: 38px;top: 130px;z-index: 7;"></image>
		</view>
	</view>
	
	<view v-else-if="type === 'B'">
		<!-- 背景 -->
		<view style="position: fixed;height: 1540rpx;">
			<image src="../../img/myflower/bac2.png" mode=""style="position: absolute;height: 1540rpx;width: 750rpx;z-index: 1;"></image>
		</view>
		<!-- 头部 -->
		<view class="" style="width: 100%;height: 137px;position: fixed;z-index: 2;<!-- background-color: #007AFF; -->opacity:0.5;">
			<!-- 返回 -->
			<navigator url="../../pages/index/main"><image src="../../img/myflower/return.png" mode=""style="width: 80rpx;height: 80rpx;position: absolute;z-index: 3; left: 26px;top:39px;"></image></navigator>
			<!-- 标题栏 -->
			<view class="" style="width: 100%;height: 45px;position: absolute;z-index: 4;bottom: 0px;<!-- background-color: #ff103c; -->opacity:0.5;">
				<image @click="qie_huan('A')" src="../../img/myflower/zhongzhi_n.png" mode=""style="position: absolute;width: 73px;height: 15px;left: 35px;bottom: 14px;z-index: 5;"></image>
				<image @click="qie_huan('B')" src="../../img/myflower/zhongzhi.png" mode=""style="position: absolute;width: 95px;height: 26px;left: 143px;bottom: 8px;z-index: 5;"></image>
				<!-- <image @click="qie_huan('C')" src="../../img/myflower/dianzhang_n.png" mode=""style="position: absolute;width: 72px;height: 15px;right: 31px;bottom: 14px;z-index: 5;"></image> -->
			</view>
		</view>
	</view>
	<view v-else-if="type === 'C'">
		<!-- 背景 -->
		<view style="position: fixed;height: 1540rpx;">
			<image src="../../img/myflower/bac3.png" mode=""style="position: absolute;height: 1540rpx;width: 750rpx;z-index: 1;"></image>
		</view>
		<!-- 头部 -->
		<view class="" style="width: 100%;height: 137px;position: fixed;z-index: 2;<!-- background-color: #007AFF; -->opacity:0.5;">
			<!-- 返回 -->
			<navigator url="../../pages/index/main"><image src="../../img/myflower/return.png" mode=""style="width: 80rpx;height: 80rpx;position: absolute;z-index: 3; left: 26px;top:39px;"></image></navigator>
			<!-- 标题栏 -->
			<view class="" style="width: 100%;height: 45px;position: absolute;z-index: 4;bottom: 0px;<!-- background-color: #ff103c; -->opacity:0.5;">
				<image @click="qie_huan('A')" src="../../img/myflower/zhongzhi_n.png" mode=""style="position: absolute;width: 73px;height: 15px;left: 35px;bottom: 14px;z-index: 5;"></image>
				<image @click="qie_huan('B')" src="../../img/myflower/history_n.png" mode=""style="position: absolute;width: 80px;height: 15px;left: 150px;bottom: 13px;z-index: 5;"></image>
				<image @click="qie_huan('C')" src="../../img/myflower/dianzhang.png" mode=""style="position: absolute;width: 95px;height: 26px;right: 20px;bottom: 8px;z-index: 5;"></image>
			</view>
		</view>
	</view>
	<view v-else-if="type === 'D'">
		<view v-if="er_wei_===1" style="position: fixed;height: 1540rpx;z-index: 20;">
			<image @click="er_wei_guan(0)" src="../../img/myflower/erwei_d.png" mode="" style="position: absolute;height: 1540rpx;width: 750rpx;z-index: 20;"></image>
		</view>
		<view v-else-if="er_wei_===0">
			<!-- 背景 -->
			<view style="position: fixed;height: 1540rpx;">
				<image src="../../img/myflower/bac4.png" mode=""style="position: absolute;height: 1540rpx;width: 750rpx;z-index: 1;"></image>
			</view>
			<!-- 头部 -->
			<image @click="er_wei(1)" src="../../img/myflower/erwei.png" mode="" style="position: fixed;width: 50px;height: 50px;right: 35px;top: 55px;z-index: 8;"></image>
			
			<view class="" style="width: 100%;height: 197px;position: fixed;z-index: 2;<!-- background-color: #007AFF; -->opacity:0.5;">
				<!-- 返回 -->
				<navigator url="../../pages/index/myflower"><image src="../../img/myflower/return.png" mode=""style="width: 80rpx;height: 80rpx;position: absolute;z-index: 3; left: 26px;top:62px;"></image></navigator>
				<!-- 标题栏 -->
				<view class="" style="width: 100%;height: 55px;position: absolute;z-index: 4;bottom: 0px;<!-- background-color: #ff103c; -->opacity:0.5;">
					<navigator url=""><image @click="qie_huan('D')" src="../../img/myflower/haoyou_p.png" mode=""style="position: absolute;width: 100px;height: 30px;left: 50px;bottom: 12px;z-index: 5;"></image></navigator>
					<navigator url=""><image @click="tan_chuang(5)" src="../../img/myflower/dianzhang_n.png" mode=""style="position: absolute;width: 80px;height: 18px;right: 50px;bottom: 18px;z-index: 5;"></image></navigator>
					
					<image src="../../img/myflower/erzi2.png" mode=""style="position: fixed;width: 280px;height: 80px;right: 38px;top: 220px;z-index: 7;"></image>
					<image src="../../img/myflower/nv.png" mode=""style="position: fixed;width: 280px;height: 80px;right: 38px;top: 320px;z-index: 7;"></image>
					<image src="../../img/myflower/jia.png" mode=""style="position: fixed;width: 40px;height: 40px;right: 160px;top: 430px;z-index: 7;"></image>
					<navigator url=""><image src="../../img/myflower/lishi.png" mode=""style="position: fixed;width: 100px;height: 30px;right: 60px;top: 230px;z-index: 8;"></image></navigator>
					<navigator url=""><image src="../../img/myflower/lishi.png" mode=""style="position: fixed;width: 100px;height: 30px;right: 60px;top: 330px;z-index: 8;"></image></navigator>
				</view>
			</view>
			<view v-if="tan === 5">
				<image src="../../img/myflower/weikaif.png" style="position: fixed;width: 280px;height: 80px;right: 38px;top: 190px;z-index: 7;"></image>
			</view>
		</view>
	</view>
	
</template>

<script>
	import socket from '../../socketio.js'
	export default {
		data() {
			return {
				stm32:'',
				type:'A',
				tan:0,tan2:0,
				tu:0,
				a:0,b:0,c:0,d:0,
				p1:0,p2:0,p3:0,p4:0,
				er_wei_:0,		// 确保websocket是打开状态
			}
		},
		onLoad: function (option) { //option为object类型，会序列化上个页面传递的参数
			        console.log(option.id); //打印出上个页面传递的参数。
			        
					var a = option.id
					if (a==1){//跳转我的种植界面
						this.tu=1
						this.p1=50;this.p2=60;this.p3=40;this.p4=30;
					}
				},
		methods: {
			
			
			//接收数据
			tcp_tx:function(contorl){
				
				},
			//发送数据
			tcp_tx2:function(contorl,tan_data,tan2_data){
				uni.request({
					url:'http://x3q3086476.51vip.biz',
					data: {
					        text: contorl//发送的变量
					    },
					method:"POST",
					success: function(){
						console.log(contorl)
					}
				})
				//增加光照
				if (contorl=="1"){
					var x1=0
					var x1_time=3000
					
					this.a=this.a+1
					if(this.a%2!=0){
						this.p4=this.p4+50
					}
					else if(this.a%2==0){
						this.p4=this.p4-50
					}
					for(;x1<40;x1++){
						if(this.p4<40){
							this.tan2=tan2_data//先显示
							setTimeout(()=>{
								this.tan2=0
							},x1_time)
							x1_time=x1_time+x1_time
						}
					}
					
					//波动
					var time4=1000
					var j1=0
					for (;j1<30;j1++){
						setTimeout(()=>{
							this.p4=this.p4+Math.floor(Math.random()*(3-0)+1)
							this.p4=this.p4-Math.floor(Math.random()*(3-0)+1)
						},time4)
						time4=time4+time4
					}
				}
				//增加空气土壤湿度
				var a=[];
				if (contorl=="2"){
					var i=0;
					var time1=3000;
					this.b=this.b+1
					var x2=0
					var x2_time=3000
					
					for (;i<20;i++){
						console.log(this.b%2)
						if(this.b%2==0){
							break;
						}
						a[i]=setTimeout(()=>{
							if(this.b%2!=0){
							this.p1=this.p1+Math.floor(Math.random()*(5-1)+1)
							this.p3=this.p3+Math.floor(Math.random()*(5-1)+1)
							console.log("xiu")
							}
						},time1)
						time1=time1+time1
					
					}
					if(this.b%2==0){
						for(i=0;i<20;i++){clearTimeout(a[i]);console.log('ok')}
					}
					for(;x2<40;x2++){
						if(this.p3<50){
							this.tan2=tan2_data//先显示
							setTimeout(()=>{
								this.tan2=0
							},x2_time)
							x2_time=x2_time+x2_time
						}
					}
					//波动
					var time5=1000
					var j3=0
					for (;j3<30;j3++){
						setTimeout(()=>{
							this.p1=this.p1+Math.floor(Math.random()*(3-0)+1)
							this.p1=this.p1-Math.floor(Math.random()*(3-0)+1)
							this.p3=this.p3+Math.floor(Math.random()*(3-0)+1)
							this.p3=this.p3-Math.floor(Math.random()*(3-0)+1)
						},time5)
						time5=time5+time5
					}
					
				}
				//降低空气温度
				if (contorl=="3"){
					var j=0;
					var time2=5000;
					this.c=this.c+1
					var x3=0
					var x3_time=3000
					for(;x3<40;x3++){
						if(this.p2>49){
							this.tan2=tan2_data//先显示
							setTimeout(()=>{
								this.tan2=0
							},x3_time)
							x3_time=x3_time+x3_time
						}
					}
					for (;j<20;j++){
						console.log(this.c,time2)
						if(this.c%2==0){
							break;
						}
						setTimeout(()=>{
							if(this.c%2!=0){
							this.p2=this.p2-Math.floor(Math.random()*(5-1)+1)
							this.p2=this.p2+Math.floor(Math.random()*(3-1)+1)
							this.p2=this.p2-Math.floor(Math.random()*(3-1)+1)
							}
							
						},time2)
						time2=time2+time2
						
						
					}
					//波动
					var time3=1000
					var j2=0
					for (;j2<30;j2++){
						setTimeout(()=>{
							this.p2=this.p2+Math.floor(Math.random()*(3-1)+1)
							this.p2=this.p2-Math.floor(Math.random()*(3-1)+1)
						},time3)
						time3=time3+time3
					}
				}
				
				//3s关闭上
				this.tan=tan_data//先显示
				setTimeout((tan_data)=>{
					this.tan=0
				},2000)
			},
			//导航栏切换
			qie_huan:function(qie){
				this.type=qie
			},
			//弹窗
			tan_chuang:function(tan_data2){
				this.tan=tan_data2//先显示
				setTimeout(()=>{
					this.tan=0
				},1500)
			},
			er_wei:function(er_wei_data){
				this.er_wei_=er_wei_data
				console.log("!!!!!!!!!!!!!!!!!!!")
			},
			er_wei_guan:function(er_wei_guan_data){
				this.er_wei_=er_wei_guan_data
				console.log("????????")
			}
			
			
			
			
			
		}
	}
</script>

<style>
	#全局样式取消滚动条
	::-webkit-scrollbar{
	
	  display: none;
	
	}
</style>
