

<script>

    let data = {
        performance: [
          'The chatbot operates well with a small number of users (up to 3), but performance degrades significantly with 20 simultaneous users',
          'This results in slow responses and often crashes, necessitating a restart of the chatbot.',
        ],
        userAnalysis: [
          'The current setup records only the latest conversation of the most recent user, which is inadequate for the project analysis goals',
          'There is a need to implement a system that can uniquely identify each user and save their individual conversation histories.',
          'There is also a need to integrate a user ID entry system before accessing the chatbot'
        ],
        hosting: [
          'There is a need for inexpensive or free hosting'
        ]
      };
    
    </script>
    
    <a href="https://community.openai.com/t/gradio-chatbot-deployment-extracting-conversation-history-simulated-conversations/699924"> Initial Inspiration for this project </a>
    
    <h2> The core project</h2>
    
    
    
    <h2> Issues Faced </h2>
    
    
    
    <table>
        <thead>
          <tr>
            <th>Performance and Scalability</th>
            <th>User Analysis</th>
            <th>Hosting</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <ul>
                {#each data.performance as item}
                  <li>{item}</li>
                {/each}
              </ul>
            </td>
            <td>
              <ul>
                {#each data.userAnalysis as item}
                  <li>{item}</li>
                {/each}
              </ul>
            </td>
            <td>
              <ul>
                {#each data.hosting as item}
                  <li>{item}</li>
                {/each}
              </ul>
            </td>
          </tr>
        </tbody>
      </table>
    
    
      <style>
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
        ul {
          padding-left: 20px;  /* Properly indent the bullet list */
          margin: 0;           /* Remove default margin for cleaner layout */
        }
        li {
          margin-bottom: 4px;  /* Space out the items slightly */
        }
      </style>
      