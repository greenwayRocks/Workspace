import React, {useState} from 'react';

function Form() {
    const [isMouseOver, setMouseOver] = useState(false);
    const [isTriggered, setTriggered] = useState(false);
    const [contact, setContact] = useState({
        fName: '',
        lName: '',
        email: ''
    });
    
    function handleChange(event) {
        const {name, value} = event.target;
        setContact(prev => {
            return {
                ...prev,
                [name]: value
            };
        })
    }
    
    function handleSubmit(event) {
        event.preventDefault();
        setTriggered(true);
    }

    function handleMouseOver() {
        setMouseOver(true);
    }

    function handleMouseOut() {
        setMouseOver(false);
    }

    return (
        <div class={(isTriggered) ? 'container right-panel-active' : 'container'}>
	<div class="form-container sign-up-container">
		<form onSubmit={handleSubmit}>
			<h1>Create Account</h1>
			<div class="social-container">
				<a href="#" class="social"><i class="fab fa-facebook-f"></i></a>
				<a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>
				<a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>
			</div>
			<span>or use your email for registration</span>
			    <input name="fName" placeholder="Your First Name" value={contact.fName} onChange={handleChange} />
                <input name="lName" placeholder="Your Last Name" value={contact.lName} onChange={handleChange} />
                <input name="email" placeholder="Your Email" value={contact.email} onChange={handleChange} />
                <button
                     onMouseOver={handleMouseOver}
                     onMouseOut={handleMouseOut}
                     style={{backgroundColor: (isMouseOver) ? 'black' : 'white'}} type="submit">Register</button>
		</form>
	</div>
	<div class="form-container sign-in-container">
		<form onSubmit={handleSubmit}>
			<h1>Sign in</h1>
			<div class="social-container">
				<a href="#" class="social"><i class="fab fa-facebook-f"></i></a>
				<a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>
				<a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>
			</div>
			<span>or use your account</span>
			<input name="fName" placeholder="Your First Name" value={contact.fName} onChange={handleChange} />
                <input name="lName" placeholder="Your Last Name" value={contact.lName} onChange={handleChange} />
                <input name="email" placeholder="Your Email" value={contact.email} onChange={handleChange} />
                <button
                     onMouseOver={handleMouseOver}
                     onMouseOut={handleMouseOut}
                     style={{backgroundColor: (isMouseOver) ? 'grey' : 'white'}} type="submit">Register</button>
		</form>
	</div>
	<div class="overlay-container">
		<div class="overlay">
			<div class="overlay-panel overlay-left">
				<h1>Welcome Back!</h1>
				<p>To keep connected with us please login with your personal info</p>
				<button class="ghost" id="signIn">Sign In</button>
			</div>
			<div class="overlay-panel overlay-right">
				<h1>Hello, Friend!</h1>
				<p>Enter your personal details and start journey with us</p>
				<button class="ghost" id="signUp">Sign Up</button>
			</div>
		</div>
	</div>
</div>
        
    );
}

export default Form;