<template>
	<div id="header">
		<div class="left">
			<!--
			<router-link to="/">Main page</router-link>
			<router-link to="/api-management">Get Your API Key!</router-link>
			-->
		</div>
		<div id="nav">
			<router-link to="/" id="logo">Cou !</router-link>
			<router-link to="/api-management" class="btn">Key Test</router-link>
			<input
				@click="showSignUp=true"
				class="btn"
				id="logout"
				name="logout"
				type="button"
				value="Logout"
			/>
			<input
				@click="showSignIn=true"
				class="btn"
				id="signin"
				name="signin"
				type="button"
				value="Sign In"
			/>
			<input
				@click="showSignUp=true"
				class="btn"
				id="signin"
				name="signup"
				type="button"
				value="Sign Up"
			/>
		</div>
		<div :class="['alert-message', alertVisible? '': 'hidden']">{{alertMessage}}</div>
		<signIn :showSignIn="showSignIn" v-on:showSignUp="showSignUp = true" v-on:showAlert="showAlert"></signIn>
		<signUp :showSignUp="showSignUp" v-on:showAlert="showAlert"></signUp>
		<hr />
		<div id="contents">
			<router-view />
		</div>
		<div id="footer">
			<div id="team15">
				<a href="https://github.com/amathon-2019/15team" target="_blank">
					<img class="icon_footer" src="@/assets/github.png" />
				</a>
				<a href="https://amathon-team15.slack.com" target="_blank">
					<img class="icon_footer" src="@/assets/slack.png" />
				</a>
				<a href="https://amathon.ga/" target="_blank">
					<img class="icon_footer" src="@/assets/amazon.png" />
				</a>
				<p>Copyright ⓒ amathon-2019/Team15 All rights Reserved</p>
			</div>
		</div>
	</div>
</template>
<script>
	import SignUp from "@/components/SignUp";
	import SignIn from "@/components/SignIn";
	import { setTimeout } from "timers";
	export default {
		components: {
			signUp: SignUp,
			signIn: SignIn
		},
		data() {
			return {
				alertMessage: "",
				alertVisible: false,
				showSignIn: false,
				showSignUp: false
			};
		},
		methods: {
			showAlert(code, message) {
				this.alertMessage = message;
				this.alertVisible = true;
				setTimeout(() => {
					this.alertVisible = false;
				}, 5000);
			}
		}
	};
</script>
<style>
	@import "https://fonts.googleapis.com/css?family=Roboto+Slab&display=swap";
	html,
	body,
	div,
	span,
	applet,
	object,
	iframe,
	h1,
	h2,
	h3,
	h4,
	h5,
	h6,
	p,
	blockquote,
	pre,
	a,
	abbr,
	acronym,
	address,
	big,
	cite,
	code,
	del,
	dfn,
	em,
	img,
	ins,
	kbd,
	q,
	s,
	samp,
	small,
	strike,
	strong,
	sub,
	sup,
	tt,
	var,
	b,
	u,
	i,
	center,
	dl,
	dt,
	dd,
	ol,
	ul,
	li,
	fieldset,
	form,
	label,
	legend,
	table,
	caption,
	tbody,
	tfoot,
	thead,
	tr,
	th,
	td,
	article,
	aside,
	canvas,
	details,
	embed,
	figure,
	figcaption,
	footer,
	header,
	hgroup,
	menu,
	nav,
	output,
	ruby,
	section,
	summary,
	time,
	mark,
	audio,
	video {
		margin: 0;
		padding: 0;
		border: 0;
		font-size: 100%;
		font: inherit;
		vertical-align: baseline;
	}

	#header,
	#footer {
		-moz-align-items: center;
		-webkit-align-items: center;
		-ms-align-items: center;
		align-items: center;
	}
	#header {
		background-color: #353535;
		cursor: default;
		height: 3.5em;
		top: 0;
		left: 0;
		line-height: 4em;
		position: fixed;
		width: 100%;
		text-align: center;
		border-bottom: 1px solid #fff;
	}
	#header #nav {
		position: absolute;
		margin-top: 8px;
		right: 2em;
		z-index: 99;
	}
	#header #nav #logo {
		color: #fff;
		font-size: 2em;
		font-family: "Roboto Slab", sans-serif;
		text-decoration: none;
		position: fixed;
		left: 1em;
		transition: all ease 1s;
	}
	#header #nav #logo:hover {
		transform: scale(1.3);
	}
	#header #logo {
		transition: all 0.4s ease 0s;
	}
	#header #logo:hover {
		color: #ffbb00;
	}
	#header .btn {
		margin-left: 10px;
		padding: 0px 10px 0px 10px;
		font-family: "Livvic", sans-serif;
		font-size: 0.8em;
		font-weight: bold;
		color: #fff;
		border: none;
		border-radius: 2px;
		cursor: pointer;
		display: inline-block;
		text-decoration: none;
		transition: all 0.4s ease 0s;
		z-index: 99;
	}
	#header .btn:hover {
		color: #ffbb00;
		-webkit-box-shadow: 0px 5px 40px -10px rgba(0, 0, 0, 0.57);
		-moz-box-shadow: 0px 5px 40px -10px rgba(0, 0, 0, 0.57);
		box-shadow: 5px 40px -10px rgba(0, 0, 0, 0.57);
		transition: all 0.4s ease 0s;
	}
	hr {
		position: fixed;
		margin-top: 80px;
		width: 100%;
		z-index: 100;
		border: 0;
		border-bottom: 1px dashed gray;
	}
	#contents {
		top: 0em;
		width: 100%;
		position: relative;
		z-index: 0;
	}
	#footer {
		position: fixed;
		background-color: rgba(256, 256, 256, 0.7);
		width: 100%;
		height: 5em;
		left: 0;
		bottom: 0;
		border: none;
	}
	#footer p {
		margin-top: -40px;
		font-family: "Livvic", sans-serif;
		font-size: 0.8em;
	}
	#footer .icon_footer {
		margin: 10px 10px 0px 10px;
		width: 20px;
		height: 20px;
	}
	.alert-message {
		width: 100%;
		height: 60px;
		position: fixed;
		bottom: 0;
		background-color: tomato;
		color: white;

		z-index: 1;
	}
	.hidden {
		display: none;
	}
</style>
