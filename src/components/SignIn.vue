<template>
	<div class="text-center">
		<v-dialog v-model="showSignIn" width="500">
			<v-card>
				<v-card-title class="headline grey lighten-2" primary-title>Sign Up</v-card-title>
				<v-text-field :rules="[rules.required]" label="ID"></v-text-field>
				<v-text-field
					v-model="password"
					:append-icon="showPassword ? 'visibility' : 'visibility_off'"
					:rules="[rules.required]"
					:type="showPassword ? 'text' : 'password'"
					label="Password"
					counter
					@click:append="showPassword = !showPassword"
				></v-text-field>

				<v-divider></v-divider>

				<v-card-actions>
					<div class="flex-grow-1"></div>
					<v-btn color="primary" text @click="$emit('showSignUp')">Sign Up</v-btn>
				</v-card-actions>
				<v-card-actions>
					<div class="flex-grow-1"></div>
					<v-btn color="primary" text @click="signIn">Sign In</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>
	</div>
</template>


<script>
	export default {
		data() {
			return {
				password: "",
				showPassword: false,
				rules: {
					required: value => !!value || "Required."
				}
			};
		},
		methods: {
			signIn: function() {
				alert(`id: ${this.id}, pw: ${this.password}`);
				this.showSignIn = false;
			}
		},
		props: ["showSignIn"]
	};
</script>
