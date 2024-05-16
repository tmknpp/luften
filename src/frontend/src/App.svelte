<script>
  import DataServices from './DataServices.svelte';

  import { curLoginRole, curLoginStatus, curLoginUser, curLoginUserID } from "./dataservices";
  import {loginValidation} from "./dataservices";

  import HomePage from './pages/Home.svelte';
  import UsersPage from './pages/Users.svelte';
  import CoreIssuesPage from './pages/CoreIssues.svelte';
  import Administration from './pages/Administration.svelte';
  import LoginPage from './pages/loginpage.svelte';

  import { Route, Router, Link, navigate } from "svelte-routing";

  let tabs = [
    { name: 'Home', route: '/home', component: HomePage, path: "/" },
    { name: 'Users', route: '/users', component: UsersPage, path: "/users" },
    { name: 'Administration', route: '/admin', component: Administration, path: "/admin/*" },
    { name: 'Core Issues', route: '/coreissues', component: CoreIssuesPage, path: '/coreissues' },
  ];

  //$: userRole = $curLoginRole
  $: userRole = (JSON.parse(localStorage.getItem('user')))?.role
  //$: loginCheck = $curLoginStatus
  $: loginCheck = (JSON.parse(localStorage.getItem('user')))?.login
  $: curUserName = $curLoginUser

  //let loginCheck = (JSON.parse(localStorage.getItem('user'))).login
  //let loginCheck = false
  console.log((JSON.parse(localStorage.getItem('user'))))
  //console.log(loginCheck,(JSON.parse(localStorage.getItem('user'))), (JSON.parse(localStorage.getItem('user'))).login )
  console.log(userRole, loginCheck, curUserName)

  async function handleLogin(event) {
    const { username, password } = event.detail;
    //console.log("login handle")

    await loginValidation(username, password)
    console.log('validated', userRole)
    let role = (JSON.parse(localStorage.getItem('user')))?.role
    if (role  === 'admin') {
      navigate('/');
    } else if (role  === 'user') {
      navigate('/users');
    }
    else{
      console.log("login failed")
      console.log(role)
    }
  }
</script>

<DataServices></DataServices>
<main style="display: flex; flex-direction: column; height: 100vh;">
  
  <div class="mainContent" style="flex: 1; min-height: 0;">
    {#if loginCheck}
      <Router>
        <nav>
          {#if userRole === 'admin'}
            <ul>
              {#each tabs as tab}
                <li><Link to={tab.route}>{tab.name}</Link></li>
              {/each}
            </ul>
          {/if}
        </nav>

        {#each tabs as tab}
          <Route path={tab.path} component={tab.component}></Route>
        {/each}
      </Router>
    {:else}
      <!-- <Router>
        <Route path="/" component={LoginPage} on:login={handleLogin}></Route>
      </Router> -->
     <LoginPage on:login={handleLogin}> </LoginPage>
      
    {/if}
  </div>
</main>

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
