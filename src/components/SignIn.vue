<template>
	<div class="text-center">
		<v-dialog v-model="showSignIn" width="500">
			<v-card class="sign-container">
				<v-card-title class="headline grey lighten-2" primary-title>Sign In</v-card-title>
				<div class="input-container">
					<span>ID:</span>
					<input v-model="id" :rules="[rules.required]" label="ID" />
				</div>
				<div class="input-container">
					<span>PASSWORD:</span>
					<input type="password" v-model="password" />
				</div>

				<v-divider></v-divider>
				<div class="action-button-container">
					<v-btn color="primary" @click="$emit('showSignUp')" text>Sign Up</v-btn>
					<v-btn color="primary" text @click="signIn">Sign In</v-btn>
				</div>
			</v-card>
		</v-dialog>
	</div>
</template>


<script>
	import axios from "axios";
	import config from "@/config";
	export default {
		data() {
			return {
				id: "",
				password: "",
				showPassword: false,
				rules: {
					required: value => !!value || "Required."
				}
			};
		},
		methods: {
			signIn: async function() {
				if (this.id.length === 0) {
					this.showAlert("error", "ID를 입력해주세요. 😥");
					return;
				}
				if (this.password.length === 0) {
					this.showAlert("error", "패스워드를 입력해주세요. 😥");
					return;
				}
				try {
					console.log(config.SERVER_HOST);
					const response = await axios.post(
						`${config.SERVER_HOST}/manage/login`,
						{
							username: this.id,
							password: this.password
						}
					);
					const data = response.data;
					localStorage.setItem("token", data.token);
					// set login
					this.showSignIn = false;
				} catch (error) {
					if (error.response.status == 400) {
						this.showAlert("error", "이미 존재하는 ID입니다. 😥");
					} else {
						this.showAlert(
							"error",
							"회원가입을 하지 못하였습니다. 잠시후에 다시 시도해 주세요. 😥"
						);
					}
				}
			},
			showAlert: function(code, message) {
				this.$emit("showAlert", code, message);
			}
		},
		props: ["showSignIn"]
	};
</script>
<style scoped>
	.sign-container {
		text-align: left;
	}
	.input-container {
		padding: 0 2em;
		margin: 0 10px;
	}
	input {
		width: 100%;
		font-size: 10pt;

		border-bottom: 2px solid black;
		transition: 1s border-bottom;
	}
	input:focus {
		outline: none;
	}
	.action-button-container {
		margin-right: 1em;
		text-align: right;
	}
</style>
