<template>
	<div class="text-center">
		<v-dialog v-model="showSignUp" width="500">
			<v-card class="sign-container">
				<v-card-title class="headline grey lighten-2" primary-title>Sign Up</v-card-title>
				<div class="input-container">
					<span>ID</span>
					<input v-model="id" label="ID" />
				</div>
				<div class="input-container">
					<span>PASSWORD</span>
					<input type="password" v-model="password" />
				</div>
				<div class="input-container">
					<span>PASSWORD CHECK</span>
					<input type="password" v-model="passwordCheck" />
				</div>

				<v-divider></v-divider>
				<div class="action-button-container">
					<v-btn color="primary" text @click="signUp">Sign Up</v-btn>
				</div>
			</v-card>
		</v-dialog>
	</div>
</template>


<script>
	import axios from "axios";
	export default {
		data() {
			return {
				id: "",
				password: "",
				passwordCheck: "",
				showPassword: false,
				showPasswordCheck: false,
				username: "",
				rules: {
					required: value => !!value || "Required.",
					minId: v => v.length >= 4 || "Min 4 characters",
					minPassword: v => v.length >= 8 || "Min 8 characters",
					emailMatch: () => "The email and password you entered don't match"
				}
			};
		},
		methods: {
			signUp: async function() {
				if (this.id.length === 0) {
					this.showAlert("error", "ID를 입력해주세요. 😥");
					return;
				} else if (this.password.length === 0) {
					this.showAlert("error", "패스워드를 입력해주세요. 😥");
					return;
				} else if (this.password !== this.passwordCheck) {
					this.showAlert(
						"error",
						"패스워드가 일치하지 않습니다. 다시 한 번 확인해 주세요. 😥"
					);
					return;
				} else {
					try {
						const response = await axios.post(
							`${process.env.SERVER_HOST}/manage/register`,
							{
								username: this.id,
								password: this.password
							}
						);
						const data = response.data;
						this.showSignUp = false;
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
				}
			},
			showAlert: function(code, message) {
				this.$emit("showAlert", code, message);
			}
		},
		props: ["showSignUp"]
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
