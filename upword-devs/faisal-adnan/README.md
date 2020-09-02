## Channel outcome
| No|Channel                    | Outcome  |   
|---|---------------------------|----------|
| 1 |  k8-performance-use-case  | Define the performance metric per target website  | 
| 2 |  k8-traffic-generator     | Kubernetes manifest file containing traffic generator and sample use cases  |
| 3 |  k8-test-data             | A storage containing malicious files |

## Workflow between channels
```ditaa {cmd=true args=["-E"]}
+--------------+            
| Files from   |            
| k8-test-data |            
| {d}          |            
+----+---------+    
     | 
     |   1. download files
     |
+----+---------------------+                    +------------------------------+     
| Traffic Generator from   | 2. upload to       | Target websites              |    
| k8-traffic-generator     |------------------->| defined by                   |    
|                          |                    | k8-performance-use-case      |    
+--------------------------+                    +------------------------------+    
     | 
     |  3. upload the test result
     |
+----+---------------------+ 4.                 +------------------------------+     
| Private storage          | validating result  | Extract the metrics and      |    
|                          |------------------->| compare with the expected    |    
|                          |                    | k8-performance-use-case      |    
+--------------------------+                    +------------------------------+    



```