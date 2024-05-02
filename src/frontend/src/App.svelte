<script>

  import DataServices from './DataServices.svelte';

  import HomePage from './pages/Home.svelte'
  import UsersPage from './pages/Users.svelte';
  import CoreIssuesPage from './pages/CoreIssues.svelte';
  import Administration from './pages/Administration.svelte';

  import { Route, Router, Link } from "svelte-routing";

  let tabs = [
 
   {name:'Home', route: '/', component: HomePage,  path:"/"},
   {name:'Users', route: '/users', component: UsersPage,  path:"/users"},
   {name:'Administration', route: '/admin', component: Administration,  path:"/admin/*"},

   {name:'Core Issues', route: '/coreissues', component: CoreIssuesPage,  path: '/coreissues' },

  ]

</script>

<DataServices> </DataServices> 
 
<main style="display: flex; flex-direction: column; height: 100vh;">
  <div class="mainContent"   style="flex: 1; min-height: 0;" >

   <Router>

     <nav>
       <ul>
         {#each tabs as tab}
             <li><Link to={tab.route}>{tab.name}</Link></li>
         {/each}
       </ul>
     </nav>
 
     {#each tabs as tab }

         <Route path={tab.path} component={tab.component}>
         </Route>
     
           
     {/each}
   </Router>
  
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
