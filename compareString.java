public static boolean compareStrings(String A, String B) {
        Map<Character,Integer> mapA = new HashMap<Character,Integer>();
        Map<Character,Integer> mapB = new HashMap<Character,Integer>();
        char[] bArr = B.toCharArray();
        char[] aArr = A.toCharArray();
        for(char c : bArr) {
            if (mapB.containsKey(c)) {
                mapB.put(c, mapB.get(c) + 1);
            } else {
                mapB.put(c, 1);
            }
        }
        for(char c : aArr) {
            if (mapA.containsKey(c)) {
                mapA.put(c, mapA.get(c) + 1);
            } else {
                mapA.put(c, 1);
            }
        }
        for(Character character : mapB.keySet()){
            if(!mapA.containsKey(character)){
                return false;
            }else{
                if(mapA.get(character) < mapB.get(character)){
                    return false;
                }
            }
        }
        return true;
    }
