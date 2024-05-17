<!-- Logout.svelte -->
<script>
    import { createEventDispatcher } from 'svelte';
    import {  navigate } from "svelte-routing"
  
    const dispatch = createEventDispatcher();
  
    function handleLogout() {
    // Clear all localStorage data
    localStorage.clear();

    // Redirect to the login page
    // You can use navigate if it's working, otherwise, use window.location.href
    navigate('/login');
    // window.location.href = '/login'; // Use this if navigate doesn't work
  }
</script>
  
  
  <button class="logout-button" on:click={handleLogout}>Logout</button>
  
  <style>
  .logout-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 4px;
    transition: background-color 0.3s;
  }
  
  .logout-button:hover {
    background-color: #0056b3;
  }
  </style>
  