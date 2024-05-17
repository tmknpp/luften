<script>
    import { auth } from "../dataservices";
    import { tick } from "svelte";

    import HomePage from './Home.svelte';
    import UsersPage from './Users.svelte';
    import CoreIssuesPage from './CoreIssues.svelte';
    import Administration from './Administration.svelte';
    import LoginPage from './loginpage.svelte';
    import Navbar from './Navbar.svelte';
    import Logout from './logout.svelte';

    import { Route, Router, Link, navigate } from "svelte-routing";
   
    $: userRole = (JSON.parse(localStorage.getItem('user')))?.role
    
    $: if (!$auth) {
        tick().then(() => navigate("/login", { replace: true }));
    }
    
    console.log("auth token", $auth)
    let tabs = [
    { name: 'Home', route: '/', component: HomePage, path: "/" },
    { name: 'Users', route: '/users', component: UsersPage, path: "/users" },
    { name: 'Administration', route: '/admin', component: Administration, path: "/admin/*" },
    { name: 'Core Issues', route: '/coreissues', component: CoreIssuesPage, path: '/coreissues' }
  
  ];
  function handleLogout() {
    // Clear all localStorage data
    localStorage.clear();

    // Redirect to the login page
    // You can use navigate if it's working, otherwise, use window.location.href
    navigate('/login');
    // window.location.href = '/login'; // Use this if navigate doesn't work
  }
</script>


<div>
    <!-- {console.log("userrole", userRole)} -->
    {#if userRole === 'admin'}
        <Navbar> </Navbar>
    {/if}

    {#each tabs as tab}
    <Route path={tab.path} component={tab.component}></Route>
   
    {/each}
</div>


<style>
    nav {
      background-color: #f8f9fa;
      padding: 10px;
    }
    
    ul {
      display: flex;
      justify-content: space-around;
      list-style-type: none;
    }
    
    li {
      cursor: pointer;
      margin-left: 30px;
      margin-right: 30px;
    }
  </style>