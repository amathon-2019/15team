<template>
	<div class="background">
		<v-card pa-5 class="BMR-container"></v-card>
	</div>
</template>

<style scoped>
	.background {
		width: 100%;
		height: 100%;

		position: fixed;
		/* display: flex;
																									align-items: center; */
		background: url("~@/assets/main-background/main-background-01.jpeg");
		background-size: cover;
		background-repeat: no-repeat;
		background-position: center center;
	}
	.BMR-container {
		width: 45%;
		/* height: 50%; */

		position: absolute;
		right: 2em;

		border-radius: 20px;

		background-color: rgba(255, 255, 255, 0.8);
	}
</style>


<script>
	export default {
		data() {
			return {
				height: 0,
				weight: 0,
				age: 0
			};
		}
	};
</script>
