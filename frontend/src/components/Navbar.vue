<template>
  <div class="bg-gray-100 font-sans w-full m-0">
    <div class="bg-white shadow">
      <div class="mx-2">
        <div class="flex items-center justify-between py-2">
          <!-- Logo -->
          <div>
            <div class="text-2xl font-semibold -mt-2">Top3Health</div>
            <!-- Circles under the logo -->
            <div class="flex mx-6">
              <div class="w-4 h-4 bg-red-500 rounded-full mx-1"></div>
              <div class="w-4 h-4 bg-blue-500 rounded-full mx-1"></div>
              <div class="w-4 h-4 bg-green-500 rounded-full mx-1"></div>
            </div>
          </div>

          <!-- Desktop menu (visible on small screens and up) -->
          <div class="hidden sm:flex sm:items-center">
            <a href="#"
               class="text-sm font-semibold hover:text-blue-500 mr-4"
               :class="{ 'text-green-500': isActive('about'), 'text-gray-800': !isActive('about') }"
               @click="setActive('about')">About</a>
            <a href="#"
               class="text-sm font-semibold hover:text-blue-500 mr-4"
               :class="{ 'text-green-500': isActive('services'), 'text-gray-800': !isActive('services') }"
               @click="setActive('services')">Services</a>
            <a href="#"
               class="text-sm font-semibold hover:text-blue-500 mr-4"
               :class="{ 'text-green-500': isActive('pricing'), 'text-gray-800': !isActive('pricing') }"
               @click="setActive('pricing')">Pricing</a>
            <a href="#"
               class="text-sm font-semibold hover:text-blue-500"
               :class="{ 'text-green-500': isActive('contact'), 'text-gray-800': !isActive('contact') }"
               @click="setActive('contact')">Contact</a>
          </div>

          <!-- Hamburger button (visible on small screens only) -->
          <div class="sm:hidden cursor-pointer" @click="toggleMenu">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
            </svg>
          </div>
        </div>

        <!-- Mobile menu (hidden or shown based on `isOpen`) -->
        <div v-show="isOpen" class="block sm:hidden bg-white border-t-2 py-2">
          <div class="flex flex-col">
            <a href="#"
               class="text-sm font-semibold hover:text-blue-500 mb-1"
               :class="{ 'text-green-500': isActive('about'), 'text-gray-800': !isActive('about') }"
               @click="setActive('about')">About</a>
            <a href="#"
               class="text-sm font-semibold hover:text-blue-500 mb-1"
               :class="{ 'text-green-500': isActive('services'), 'text-gray-800': !isActive('services') }"
               @click="setActive('services')">Services</a>
            <a href="#"
               class="text-sm font-semibold hover:text-blue-500 mb-1"
               :class="{ 'text-green-500': isActive('pricing'), 'text-gray-800': !isActive('pricing') }"
               @click="setActive('pricing')">Pricing</a>
            <a href="#"
               class="text-sm font-semibold hover:text-blue-500 mb-1"
               :class="{ 'text-green-500': isActive('contact'), 'text-gray-800': !isActive('contact') }"
               @click="setActive('contact')">Contact</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// Define the isOpen state to control mobile menu visibility
const isOpen = ref(false)

// Function to toggle the mobile menu visibility
const toggleMenu = () => {
  isOpen.value = !isOpen.value
}

// Function to set active link (you can call this when a user clicks a link)
const activeLink = ref('home')

// Function to set the active link
const setActive = (link) => {
  activeLink.value = link
}

// Function to check if the link is active
const isActive = (link) => {
  return activeLink.value === link
}
</script>

<style scoped>
/* Optional: You can add custom styles here if needed */
</style>
