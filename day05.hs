import Data.List

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                  "" -> []
                  s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'

myParse :: [String] -> [[Integer]]
myParse [] = []
myParse (x:xs) = [a .. b] : myParse xs
                            where a = read (head (wordsWhen (=='-') x)) :: Integer
                                  b = read (last (wordsWhen (=='-') x)) :: Integer

myFindIndices :: Char -> String -> Int
myFindIndices x s = head (elemIndices x s)

parseSetup :: String -> Int -> String
parseSetup s i = 
  if x `elem` ['A'..'Z'] then [x]
  else ""
    where x = s!!i


main = do
        contents <- readFile "input.txt"
        let rows = wordsWhen (=='\n') contents
        let setup = filter ( not . isInfixOf "move") rows
        let ins = filter (isInfixOf "move") rows
        let lastSetup = last setup
        let initSetup = init setup
        let numberOfStacks = read [(last (init lastSetup))] :: Integer
        let stacks = map show [1..numberOfStacks]
       
        let stackIndex = [myFindIndices (head x) lastSetup | x <- stacks]
        print(stackIndex)
        print(initSetup)
        let base = ["" | x <- [1..numberOfStacks]]
        print(base)
