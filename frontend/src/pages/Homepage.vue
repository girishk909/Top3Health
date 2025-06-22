<template>
  <div class="flex justify-center items-center bg-gray-50 relative py-8 h-screen">
    <!-- Background image with opacity -->
    <div class="absolute inset-0 bg-no-repeat bg-cover bg-center" style="background-image: url('https://cdn.vectorstock.com/i/1000v/57/00/healthy-lifestyle-cartoon-composition-vector-31785700.jpg'); opacity: 0.2;"></div>
    
    <div class="bg-white rounded-lg shadow-xl overflow-hidden w-full max-w-md relative z-10 -mt-36">
      <!-- Form Container with Slider Animation -->
      <div class="relative">
        <!-- Form Header with Tabs -->
        <div class="flex text-lg border-b">
          <button 
            @click="activeTab = 'login'" 
            class="w-1/2 py-4 font-medium transition-colors duration-300"
            :class="activeTab === 'login' ? 'text-blue-600' : 'text-gray-500 hover:text-gray-700'"
          >
            Login
          </button>
          <button 
            @click="activeTab = 'signup'" 
            class="w-1/2 py-4 font-medium transition-colors duration-300"
            :class="activeTab === 'signup' ? 'text-blue-600' : 'text-gray-500 hover:text-gray-700'"
          >
            Sign Up
          </button>
        </div>
        
        <!-- Animated Slider -->
        <div 
          class="h-1 bg-blue-500 transition-all duration-300 ease-in-out"
          :style="{ width: '50%', marginLeft: activeTab === 'login' ? '0' : '50%' }"
        ></div>
        
        <!-- Green accent line at the top -->
        <div class="h-1 bg-green-400 w-full"></div>
        
        <!-- Login Form -->
        <div 
          v-if="activeTab === 'login'"
          class="p-8 transition-all duration-500"
          style="min-height: 450px;"
        >
          <h2 class="text-2xl font-bold mb-6 text-gray-800">Welcome Back</h2>
          
          <form @submit.prevent="handleLogin">
            <div class="mb-4">
              <label class="block text-gray-700 text-sm font-medium mb-2" for="login-email">
                Email
              </label>
              <input 
                id="login-email"
                v-model="loginForm.email"
                type="email" 
                class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
                :class="errors.loginEmail ? 'border-red-500' : 'border-gray-300'"
                placeholder="your@email.com"
                required
              />
              <p v-if="errors.loginEmail" class="text-red-500 text-xs mt-1">{{ errors.loginEmail }}</p>
            </div>
            
            <div class="mb-4">
              <div class="flex justify-between items-center mb-2">
                <label class="text-gray-700 text-sm font-medium" for="login-password">
                  Password
                </label>
                <a href="#" class="text-sm text-blue-600 hover:text-blue-800">Forgot Password?</a>
              </div>
              <input 
                id="login-password"
                v-model="loginForm.password"
                type="password" 
                class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
                :class="errors.loginPassword ? 'border-red-500' : 'border-gray-300'"
                placeholder="••••••••"
                required
              />
              <p v-if="errors.loginPassword" class="text-red-500 text-xs mt-1">{{ errors.loginPassword }}</p>
            </div>
            
            <div class="mb-5">
              <label class="flex items-center">
                <input type="checkbox" class="form-checkbox h-4 w-4 text-green-500 rounded" />
                <span class="ml-2 text-sm text-gray-700">Remember me</span>
              </label>
            </div>
            
            <button 
              type="submit" 
              class="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors duration-300 flex justify-center items-center"
            >
              <span>Login</span>
            </button>
          </form>
          
          <div class="mt-5 text-center">
            <p class="text-sm text-gray-600">
              Don't have an account? 
              <button 
                @click="activeTab = 'signup'" 
                class="text-green-500 hover:text-green-600 font-medium"
              >
                Sign up
              </button>
            </p>
          </div>
        </div>
        
        <!-- Signup Form -->
        <div 
          v-if="activeTab === 'signup'"
          class="p-8 transition-all duration-500"
          style="min-height: 450px;"
        >
          <h2 class="text-2xl font-bold mb-5 text-gray-800">Create Account</h2>
          
          <form @submit.prevent="handleSignup">
            <div class="mb-4">
              <label class="block text-gray-700 text-sm font-medium mb-2" for="signup-name">
                Full Name
              </label>
              <input 
                id="signup-name"
                v-model="signupForm.name"
                type="text" 
                class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
                :class="errors.signupName ? 'border-red-500' : 'border-gray-300'"
                placeholder="John Doe"
                required
              />
              <p v-if="errors.signupName" class="text-red-500 text-xs mt-1">{{ errors.signupName }}</p>
            </div>
            
            <div class="mb-4">
              <label class="block text-gray-700 text-sm font-medium mb-2" for="signup-email">
                Email
              </label>
              <input 
                id="signup-email"
                v-model="signupForm.email"
                type="email" 
                class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
                :class="errors.signupEmail ? 'border-red-500' : 'border-gray-300'"
                placeholder="your@email.com"
                required
              />
              <p v-if="errors.signupEmail" class="text-red-500 text-xs mt-1">{{ errors.signupEmail }}</p>
            </div>
            
            <div class="mb-4">
              <label class="block text-gray-700 text-sm font-medium mb-2" for="signup-password">
                Password
              </label>
              <input 
                id="signup-password"
                v-model="signupForm.password"
                type="password" 
                class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
                :class="errors.signupPassword ? 'border-red-500' : 'border-gray-300'"
                placeholder="••••••••"
                required
              />
              <p v-if="errors.signupPassword" class="text-red-500 text-xs mt-1">{{ errors.signupPassword }}</p>
            </div>
            
            <div class="mb-5">
              <label class="flex items-center">
                <input 
                  type="checkbox" 
                  v-model="signupForm.agreeTerms"
                  class="form-checkbox h-4 w-4 text-green-500 rounded"
                />
                <span class="ml-2 text-sm text-gray-700">
                  I agree to the <a href="#" class="text-green-500 hover:text-green-600">Terms of Service</a> 
                  and <a href="#" class="text-green-500 hover:text-green-600">Privacy Policy</a>
                </span>
              </label>
              <p v-if="errors.agreeTerms" class="text-red-500 text-xs mt-1">{{ errors.agreeTerms }}</p>
            </div>
            
            <button 
              type="submit" 
              class="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors duration-300 flex justify-center items-center"
            >
              <span>Create Account</span>
            </button>
          </form>
          
          <div class="mt-5 text-center">
            <p class="text-sm text-gray-600">
              Already have an account? 
              <button 
                @click="activeTab = 'login'" 
                class="text-green-500 hover:text-green-600 font-medium"
              >
                Login
              </button>
            </p>
          </div>
        </div>
        
        <!-- Green accent decoration at the bottom -->
        <div class="h-2 bg-gradient-to-r from-green-400 via-green-500 to-green-400"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeTab: 'login',
      loginForm: {
        email: '',
        password: ''
      },
      signupForm: {
        name: '',
        email: '',
        password: '',
        agreeTerms: false
      },
      errors: {}
    }
  },
  methods: {
    handleLogin() {
      // Reset errors
      this.errors = {};
      let hasErrors = false;
      
      // Simple validation
      if (!this.loginForm.email) {
        this.errors.loginEmail = 'Email is required';
        hasErrors = true;
      } else if (!this.validateEmail(this.loginForm.email)) {
        this.errors.loginEmail = 'Please enter a valid email address';
        hasErrors = true;
      }
      
      if (!this.loginForm.password) {
        this.errors.loginPassword = 'Password is required';
        hasErrors = true;
      } else if (this.loginForm.password.length < 6) {
        this.errors.loginPassword = 'Password must be at least 6 characters';
        hasErrors = true;
      }
      
      if (!hasErrors) {
        // Handle successful login
        alert('Login successful!');
        // Here you would typically call your API to log the user in
      }
    },
    
    handleSignup() {
      // Reset errors
      this.errors = {};
      let hasErrors = false;
      
      // Simple validation
      if (!this.signupForm.name) {
        this.errors.signupName = 'Full name is required';
        hasErrors = true;
      }
      
      if (!this.signupForm.email) {
        this.errors.signupEmail = 'Email is required';
        hasErrors = true;
      } else if (!this.validateEmail(this.signupForm.email)) {
        this.errors.signupEmail = 'Please enter a valid email address';
        hasErrors = true;
      }
      
      if (!this.signupForm.password) {
        this.errors.signupPassword = 'Password is required';
        hasErrors = true;
      } else if (this.signupForm.password.length < 6) {
        this.errors.signupPassword = 'Password must be at least 6 characters';
        hasErrors = true;
      }
      
      if (!this.signupForm.agreeTerms) {
        this.errors.agreeTerms = 'You must agree to the Terms of Service and Privacy Policy';
        hasErrors = true;
      }
      
      if (!hasErrors) {
        // Handle successful signup
        alert('Account created successfully!');
        // Here you would typically call your API to register the user
      }
    },
    
    validateEmail(email) {
      // Simple email validation regex
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(email);
    }
  }
}
</script>

<style>
/* Add any additional custom styles here if needed */
/* The transition properties are already added inline */
</style>
