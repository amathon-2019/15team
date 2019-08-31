<template>
	<div class="background">
		<v-card pa-5 class="BMR-container">
			<h1>⬇️️️치킨 한 마리 무료 배송 코드 받기⬇️</h1>
			<button class="coupon-button">🐔쿠폰 발급 받기🐔</button>
			<h2>🔥실시간 쿠폰 수량: {{couponLeft}}</h2>
			<v-card v-if="couponCode">
				<h1>{{couponCode}}</h1>
			</v-card>
		</v-card>
	</div>
</template>

<style scoped>
	.background {
		width: 100%;
		height: 100%;

		position: fixed;
		display: flex;
		align-items: center;
		justify-content: center;
		background: url("~@/assets/main-background/main-background-01.jpeg");
		background-size: cover;
		background-repeat: no-repeat;
		background-position: center center;
	}
	.BMR-container {
		/* height: 50%; */
		width: 50%;

		background-color: rgba(255, 255, 255, 0.8);
	}
	.coupon-button {
		padding: 0 30px;
		margin: 1em;
		border-radius: 10px;
		background-color: #ddc252;
	}
	.coupon-button:focus {
		outline: none;
	}
</style>


<script>
	import { setInterval } from "timers";
	import config from "@/config";
	import axios from "axios";
	export default {
		data() {
			return {
				height: 0,
				weight: 0,
				age: 0,
				couponCode: "test",
				couponLeft: 0
			};
		},
		methods: {
			getRealtimeLeftCouponNumber: function() {
				setInterval(() => {
					const response = axios.get(`${config}/manage/key/`);
				}, 2000);
			}
		},
		mounted() {
			this.getRealtimeLeftCouponNumber();
		}
	};
</script>
