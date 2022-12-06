findMarker :: String -> Int -> Int -> Int -> Int 
findMarker s l start end
  | (allDifferent(subList) && length subList == l) = end
  | otherwise                                      = findMarker s l (start + 1) (end + 1)
    where subList = drop start . take end $ s

allDifferent :: String -> Bool
allDifferent [] = True
allDifferent (x:xs) = x `notElem` xs && allDifferent xs

main = do
        contents <- readFile "input.txt"
        let rows = lines contents
        let packetStart = findMarker (head rows) 4 0 4
        let messageStart = findMarker (head rows) 14 0 14
        print(packetStart)
        print(messageStart)
