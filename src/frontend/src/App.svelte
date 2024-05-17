<script>
  import DataServices from './DataServices.svelte';
  import { auth } from "./dataservices";

  //import { curLoginRole, curLoginStatus, curLoginUser, curLoginUserID } from "./dataservices";
  //import {loginValidation} from "./dataservices";

 // import { curLoginRole, curLoginStatus, curLoginUser, curLoginUserID } from "./dataservices";
 // import {loginValidation} from "./dataservices";

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
    { name: 'Home', route: '/', component: HomePage, path: "/" },
    { name: 'Users', route: '/users', component: UsersPage, path: "/users" },
    { name: 'Administration', route: '/admin', component: Administration, path: "/admin/*" },
    { name: 'Core Issues', route: '/coreissues', component: CoreIssuesPage, path: '/coreissues' },
  ];

</script>

<DataServices></DataServices>

<main>
  <div class="mainContent" style="flex: 1; min-height:0;">

    <Router>
      <PublicRouteGuard />
      <PrivateRouteGuard />
    </Router>

  </div>
</main>


