<script>

import { listPupils } from "../../dataservices";
import { createPupil, deletePupil } from "../../dataservices";
import { exportPupilMessages } from "../../dataservices";

import { refreshPupils } from "../../dataservices";
$: users = $listPupils

let selectedUsers  = [""]

let newUser = '';
let newPassword = '';

function toDateTime(secs) {
    var t = new Date(0)
    t.setSeconds(secs)
    return t
}
  // Function to add a new user
async  function createUser() {
    if (newUser.trim() !== '' && !users.includes(newUser)) {
        
        await createPupil(newUser, newPassword)
        await refreshPupils()

        newUser = ''; // Reset the input after adding
        newPassword = '';
    }
  }

  // Function to delete the selected user
  async function deleteUser() {

    for (const selectedUser of selectedUsers) {
       await deletePupil(selectedUser[0]);
    }
    await refreshPupils()

  }

  // Function to export pupil chat history
  async function exportUserMessages(user) {
    if (user !== '' && users.includes(user)){
      await exportPupilMessages(user[0])
    }
  }
</script>


<div>
  <h2> User Administration </h2>

</div>

<div class="container">
    <div class="user-select">
      {#each users as user}
        <label> 
          <input type="checkbox" bind:group={selectedUsers} value={user} />
          {user[1]}
        </label>
      {/each}



       <!-- Form to create new user -->
      <input type="text" bind:value={newUser} placeholder="New user name" />
      <input type="text" bind:value={newPassword} placeholder="New user password" />

      <div class="button-container">
        <button on:click={createUser}>Create User</button>
        {#if users.length > 0}
            <button on:click={deleteUser} disabled={users.length === 0}>Delete Selected User/s</button>
        {/if}
      </div>

    </div>

    
    <div class="user-content">
        {#if selectedUsers.length > 0}


        <table>
            <thead>
              <tr>
                {#each selectedUsers as user}
                   <th> {user[1]} </th>
                {/each}

              </tr>
            </thead>
            <tbody>
                <tr>
                    {#each selectedUsers as user}
                        <td> {user[0]} </td>
                    {/each}
                </tr>
                <tr>
                    {#each selectedUsers as user}
                        <td> {toDateTime(user[2])} </td>
                    {/each}
                </tr>

                <tr>
                    {#each selectedUsers as user}
                        <td> Tokens Consumed </td>
                    {/each}
                </tr>

                <tr>
                    {#each selectedUsers as user}
                        <td> Assessment </td>
                    {/each}
                </tr>

                <tr>
                  {#each selectedUsers as user}
                    <td>
                      <div class="button-container">
                        <button on:click={exportUserMessages(user)}>Export Chat</button>
                      </div>
                    </td>
                  {/each}
                </tr>

            </tbody>
          </table>
        

        {/if}
    </div>
  </div>



  <style>
    .container {
      display: flex;
      width: 100%;
    }
  
    
    .button-container {
     display: flex; /* Enables flexbox layout */
     justify-content: space-between; /* Spreads buttons across available space */
    margin-top: 10px; /* Top margin for spacing */
  }
    .user-select {
      width: 20%;
      padding: 10px;
    }
    
    .user-content {
      width: 80%;
      padding: 10px;
      background-color: #282727; /* Light gray background for the content area */
    }
    
    label {
      display: block; /* Makes labels stack vertically */
      margin-bottom: 10px; /* Adds space between each label */
    }

    table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 8px;
      text-align: left;
    }
    th {
      background-color: #a7a9a9;
    }

  </style>
  