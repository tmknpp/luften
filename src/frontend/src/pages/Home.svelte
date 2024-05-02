<script>
import { listPupils } from "../dataservices";

$: users = $listPupils

let sortedCreateTime = []

function handleUsersUpdate() {
  sortedCreateTime = []

  for (const pupil of users) {
     sortedCreateTime.push(parseInt(pupil[2]))
  }

  sortedCreateTime.sort((a,b) => a-b)

}

function toDateTime(secs) {
    var t = new Date(0)
    t.setSeconds(secs)
    return t
}

$: if (users) {
    handleUsersUpdate();
  }

</script>

<a href="https://community.openai.com/t/gradio-chatbot-deployment-extracting-conversation-history-simulated-conversations/699924"> Initial Inspiration for this project </a>

<div>
  <h2> Prime Directive</h2>
  Place Holder 
  
</div>

<div>
    
</div>
<div>
  <h2> Overall Stats </h2>
  <div>
    There are currently {users.length} users in the system.
  </div>
  <div> 
    The users have been created between {toDateTime(sortedCreateTime[0])} and {toDateTime(sortedCreateTime[sortedCreateTime.length -1 ])}
  </div>
</div>


  <style>
    
  </style>
  