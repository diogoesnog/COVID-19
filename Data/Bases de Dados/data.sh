#!/bin/bash

curl 'https://wabi-west-europe-d-primary-api.analysis.windows.net/public/reports/querydata?synchronous=true' \
  -H 'Connection: keep-alive' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'RequestId: 3176e30c-c040-4f9c-6b6b-a02847df9cb8' \
  -H 'X-PowerBI-ResourceKey: 6e2a3269-ab56-40ef-859b-f749ed24f6fe' \
  -H 'ActivityId: 8d414eb0-40fc-42b0-a83f-db4edb65b1cb' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Origin: https://app.powerbi.com' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://app.powerbi.com/view?r=eyJrIjoiNmUyYTMyNjktYWI1Ni00MGVmLTg1OWItZjc0OWVkMjRmNmZlIiwidCI6IjczYzc3MWNkLTFjNzUtNDc5OS1hYTQwLTFjOWZmM2NmM2U1ZSIsImMiOjl9' \
  -H 'Accept-Language: pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7' \
  --data-binary $'{"version":"1.0.0","queries":[{"Query":{"Commands":[{"SemanticQueryDataShapeCommand":{"Query":{"Version":2,"From":[{"Name":"f1","Entity":"FORWARDKEYS_BOOKING_EU"},{"Name":"f","Entity":"FORWARDKEYS_BOOKING_PT"},{"Name":"d","Entity":"D_TEMPO"}],"Select":[{"Column":{"Expression":{"SourceRef":{"Source":"f1"}},"Property":"Data"},"Name":"FORWARDKEYS_BOOKING_EU.Data"},{"Measure":{"Expression":{"SourceRef":{"Source":"f1"}},"Property":"% Reservas EU - Variação dia a dia"},"Name":"FORWARDKEYS_BOOKING_EU.% Reservas EU - Var"}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"Data"}}],"Values":[[{"Literal":{"Value":"datetime\'2020-03-13T00:00:00\'"}}]]}}},{"Condition":{"Between":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"d"}},"Property":"DES_DIA"}},"LowerBound":{"DateSpan":{"Expression":{"Now":{}},"TimeUnit":0}},"UpperBound":{"DateSpan":{"Expression":{"DateAdd":{"Expression":{"DateAdd":{"Expression":{"Now":{}},"Amount":-1,"TimeUnit":0}},"Amount":1,"TimeUnit":2}},"TimeUnit":0}}}}}]},"Binding":{"Primary":{"Groupings":[{"Projections":[0,1]}]},"DataReduction":{"DataVolume":4,"Primary":{"BinnedLineSample":{}}},"Version":1}}}]},"QueryId":"","ApplicationContext":{"DatasetId":"64e94dc9-a795-419c-95aa-98fe52509c94","Sources":[{"ReportId":"8639b885-081e-40ee-a2b3-a7ade2da5d0c"}]}}],"cancelQueries":[],"modelId":221950}' \
  --compressed --output dadosUE.json

curl 'https://wabi-west-europe-d-primary-api.analysis.windows.net/public/reports/querydata?synchronous=true' \
  -H 'Connection: keep-alive' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'RequestId: f6ac17cf-a670-4cb9-e057-2a81a300fc0f' \
  -H 'X-PowerBI-ResourceKey: 6e2a3269-ab56-40ef-859b-f749ed24f6fe' \
  -H 'ActivityId: 70a256ed-6ce7-423e-a7f5-e344c5a77385' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Origin: https://app.powerbi.com' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://app.powerbi.com/view?r=eyJrIjoiNmUyYTMyNjktYWI1Ni00MGVmLTg1OWItZjc0OWVkMjRmNmZlIiwidCI6IjczYzc3MWNkLTFjNzUtNDc5OS1hYTQwLTFjOWZmM2NmM2U1ZSIsImMiOjl9' \
  -H 'Accept-Language: pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7' \
  --data-binary '{"version":"1.0.0","queries":[{"Query":{"Commands":[{"SemanticQueryDataShapeCommand":{"Query":{"Version":2,"From":[{"Name":"f","Entity":"FORWARDKEYS_BOOKING_PT"},{"Name":"d","Entity":"D_TEMPO"}],"Select":[{"Column":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"Data"},"Name":"FORWARDKEYS_BOOKING_PT.Data"},{"Measure":{"Expression":{"SourceRef":{"Source":"f"}},"Property":"% Reservas PT - Variação dia a dia"},"Name":"FORWARDKEYS_BOOKING_PT.% Reservas PT - Variação dia a dia"}],"Where":[{"Condition":{"Between":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"d"}},"Property":"DES_DIA"}},"LowerBound":{"DateSpan":{"Expression":{"Now":{}},"TimeUnit":0}},"UpperBound":{"DateSpan":{"Expression":{"DateAdd":{"Expression":{"DateAdd":{"Expression":{"Now":{}},"Amount":-1,"TimeUnit":0}},"Amount":1,"TimeUnit":2}},"TimeUnit":0}}}}}]},"Binding":{"Primary":{"Groupings":[{"Projections":[0,1]}]},"DataReduction":{"DataVolume":4,"Primary":{"BinnedLineSample":{}}},"Version":1}}}]},"CacheKey":"{\"Commands\":[{\"SemanticQueryDataShapeCommand\":{\"Query\":{\"Version\":2,\"From\":[{\"Name\":\"f\",\"Entity\":\"FORWARDKEYS_BOOKING_PT\"},{\"Name\":\"d\",\"Entity\":\"D_TEMPO\"}],\"Select\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"f\"}},\"Property\":\"Data\"},\"Name\":\"FORWARDKEYS_BOOKING_PT.Data\"},{\"Measure\":{\"Expression\":{\"SourceRef\":{\"Source\":\"f\"}},\"Property\":\"% Reservas PT - Variação dia a dia\"},\"Name\":\"FORWARDKEYS_BOOKING_PT.% Reservas PT - Variação dia a dia\"}],\"Where\":[{\"Condition\":{\"Between\":{\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"d\"}},\"Property\":\"DES_DIA\"}},\"LowerBound\":{\"DateSpan\":{\"Expression\":{\"Now\":{}},\"TimeUnit\":0}},\"UpperBound\":{\"DateSpan\":{\"Expression\":{\"DateAdd\":{\"Expression\":{\"DateAdd\":{\"Expression\":{\"Now\":{}},\"Amount\":-1,\"TimeUnit\":0}},\"Amount\":1,\"TimeUnit\":2}},\"TimeUnit\":0}}}}}]},\"Binding\":{\"Primary\":{\"Groupings\":[{\"Projections\":[0,1]}]},\"DataReduction\":{\"DataVolume\":4,\"Primary\":{\"BinnedLineSample\":{}}},\"Version\":1}}}]}","QueryId":"","ApplicationContext":{"DatasetId":"64e94dc9-a795-419c-95aa-98fe52509c94","Sources":[{"ReportId":"8639b885-081e-40ee-a2b3-a7ade2da5d0c"}]}}],"cancelQueries":[],"modelId":221950}' \
  --compressed --output dadosPT.json