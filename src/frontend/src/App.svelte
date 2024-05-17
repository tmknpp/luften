<script>
  import DataServices from './DataServices.svelte';
  import { auth } from "./dataservices";

  //import { curLoginRole, curLoginStatus, curLoginUser, curLoginUserID } from "./dataservices";
  //import {loginValidation} from "./dataservices";

  import HomePage from './pages/Home.svelte';
  import UsersPage from './pages/Users.svelte';
  import CoreIssuesPage from './pages/CoreIssues.svelte';
  import Administration from './pages/Administration.svelte';
  import LoginPage from './pages/loginpage.svelte';
  import PrivateRouteGuard from './pages/PrivateRouteGuard.svelte';
  import PublicRouteGuard from './pages/PublicRouteGuard.svelte';
  import Navbar from './pages/Navbar.svelte';

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
 // $: loginCheck = (JSON.parse(localStorage.getItem('user')))?.login
  //$: curUserName = (JSON.parse(localStorage.getItem('user')))?.name

  //let loginCheck = (JSON.parse(localStorage.getItem('user'))).login
  //let loginCheck = false
  //console.log((JSON.parse(localStorage.getItem('user'))))
  //console.log(loginCheck,(JSON.parse(localStorage.getItem('user'))), (JSON.parse(localStorage.getItem('user'))).login )
  //console.log(userRole, curUserName)

  // async function handleLogin(event) {
  //   const { username, password } = event.detail;
  //   //console.log("login handle")

  //   await loginValidation(username, password)
  //   console.log('validated', userRole)
  //   let role = (JSON.parse(localStorage.getItem('user')))?.role || null
  //   if (role  === 'admin') {
  //     navigate('/');
  //   } else if (role  === 'user') {
  //     navigate('/users');
  //   }
  //   else{
  //     console.log("login failed")
  //     console.log(role)
  //   }
  // }
</script>

<DataServices></DataServices>
<!-- <main style="display: flex; flex-direction: column; height: 100vh;">
  
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
    {:else}>
     <LoginPage on:login={handleLogin}> </LoginPage>
      
    {/if}
  </div>
</main> -->

<main>
  <div class="mainContent" style="flex: 1; min-height:0;">
    
    <!-- <Router>
        <Route  path="/login" component={LoginPage} />

      <PrivateRouteGuard > 
        {#each tabs as tab}
        <Route path={tab.path} component={tab.component} ></Route>
      {/each}
      </PrivateRouteGuard>
      
    </Router> -->
    

    <Router>
      <PublicRouteGuard />
      <PrivateRouteGuard />
    </Router>

  </div>
</main>


