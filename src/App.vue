<template>
	<div id="header">
		<div class="left">
			<router-link to="/">Main page</router-link>
			<router-link to="/api-management">Get Your API Key!</router-link>
		</div>
		<div id="right">
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
		<router-view />
		<signIn :showSignIn="showSignIn"></signIn>
		<signUp :showSignUp="showSignUp"></signUp>
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
	export default {
		components: {
			signUp: SignUp,
			signIn: SignIn
		},
		data() {
			return {
				showSignIn: false,
				showSignUp: false
			};
		}
	};
</script>


<style>
	@import "https://fonts.googleapis.com/css?family=Livvic&display=swap";
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
	}
	#header #right {
		position: absolute;
		margin-top: -8px;
		right: 2em;
	}
	#header .btn {
		margin-left: 10px;
		padding: 4px 15px 4px 15px;
		background-color: #fff;
		font-family: "Livvic", sans-serif;
		font-size: 0.7em;
		color: #000;
		border: none;
		border-radius: 2px;
		cursor: pointer;
		display: inline-block;
		transition: all 0.4s ease 0s;
	}
	#header .btn:hover {
		background-color: #ffbb00;
		-webkit-box-shadow: 0px 5px 40px -10px rgba(0, 0, 0, 0.57);
		-moz-box-shadow: 0px 5px 40px -10px rgba(0, 0, 0, 0.57);
		box-shadow: 5px 40px -10px rgba(0, 0, 0, 0.57);
		transition: all 0.4s ease 0s;
	}
	#intro {
		top: 3.5em;
		width: 100%;
		position: fixed;
	}
	#footer {
		position: fixed;
		background-color: #eee;
		width: 100%;
		height: 7em;
		left: 0;
		bottom: 0;
		border: none;
	}
	#footer p {
		margin-top: -30px;
		font-family: "Livvic", sans-serif;
		font-size: 0.8em;
	}
	#footer .icon_footer {
		margin: 30px 10px 0px 10px;
		width: 30px;
		height: 30px;
	}
</style>
