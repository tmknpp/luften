<script>
    import { Link } from "svelte-routing";
    import HomePage from './Home.svelte';
    import UsersPage from './Users.svelte';
    import CoreIssuesPage from './CoreIssues.svelte';
    import Administration from './Administration.svelte';
    import LoginPage from './loginpage.svelte';
    import Logout from "./logout.svelte";

    let loginCheck = (JSON.parse(localStorage.getItem('user')))?.login

    let tabs = [
    { name: 'Home', route: '/', component: HomePage, path: "/" },
    { name: 'Users', route: '/users', component: UsersPage, path: "/users" },
    { name: 'Administration', route: '/admin', component: Administration, path: "/admin/*" },
    { name: 'Core Issues', route: '/coreissues', component: CoreIssuesPage, path: '/coreissues' },
    
    ];
</script>

<div>
  <nav>
    <ul>
      {#each tabs as tab}
        <li><Link to={tab.route}>{tab.name}</Link></li>
      {/each}
      <li><Logout /></li> <!-- Include the LogoutButton in the navbar -->
    </ul>
  </nav>
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