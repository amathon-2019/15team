<template>
	<div class="text-center">
		<v-dialog v-model="showSignUp" width="500">
			<v-card>
				<v-card-title class="headline grey lighten-2" primary-title>Sign Up</v-card-title>
				<v-text-field :rules="[rules.required]" v-model="username" label="User name"></v-text-field>
				<v-text-field :rules="[rules.required, rules.minId]" v-model="id" label="ID"></v-text-field>
				<v-text-field
					v-model="password"
					:append-icon="showPassword ? 'visibility' : 'visibility_off'"
					:rules="[rules.required, rules.minPassword]"
					:type="showPassword ? 'text' : 'password'"
					label="Password"
					hint="At least 8 characters"
					counter
					@click:append="showPassword = !showPassword"
				></v-text-field>
				<v-text-field
					v-model="passwordCheck"
					:append-icon="showPasswordCheck ? 'visibility' : 'visibility_off'"
					:rules="[rules.required, rules.minPassword]"
					:type="showPasswordCheck ? 'text' : 'password'"
					label="Password check"
					hint="At least 8 characters"
					counter
					@click:append="showPasswordCheck = !showPasswordCheck"
				></v-text-field>

				<v-divider></v-divider>

				<v-card-actions>
					<div class="flex-grow-1"></div>
					<v-btn color="primary" text @click="showSignUp = false">Sign Up</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>
	</div>
</template>


<script>
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
		props: ["showSignUp"]
	};
</script>
