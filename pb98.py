# -------------------------------------------------------------------------------
# Name:        pb98
# Purpose:     project euler
# Created:     11/07/2015
# -------------------------------------------------------------------------------

import math
import itertools
import time
import sys


def issqr(n):
    return math.sqrt(n) == math.floor(math.sqrt(n))


def ordonnemot(s):
    temp = sorted(s)
    w = ''
    for i in range(0, len(temp)):
        w += temp[i]
    return w


def replace_all(text, dic):
    nouveautext = (text + '.')[:-1]
    for i, j in dic.items():
        nouveautext = nouveautext.replace(i, j)
    return nouveautext


def main():
    start = time.perf_counter()
    words = ['A', 'ABILITY', 'ABLE', 'ABOUT', 'ABOVE', 'ABSENCE', 'ABSOLUTELY', 'ACADEMIC', 'ACCEPT', 'ACCESS',
             'ACCIDENT',
             'ACCOMPANY', 'ACCORDING', 'ACCOUNT', 'ACHIEVE', 'ACHIEVEMENT', 'ACID', 'ACQUIRE', 'ACROSS', 'ACT',
             'ACTION',
             'ACTIVE', 'ACTIVITY', 'ACTUAL', 'ACTUALLY', 'ADD', 'ADDITION', 'ADDITIONAL', 'ADDRESS', 'ADMINISTRATION',
             'ADMIT', 'ADOPT', 'ADULT', 'ADVANCE', 'ADVANTAGE', 'ADVICE', 'ADVISE', 'AFFAIR', 'AFFECT', 'AFFORD',
             'AFRAID',
             'AFTER', 'AFTERNOON', 'AFTERWARDS', 'AGAIN', 'AGAINST', 'AGE', 'AGENCY', 'AGENT', 'AGO', 'AGREE',
             'AGREEMENT',
             'AHEAD', 'AID', 'AIM', 'AIR', 'AIRCRAFT', 'ALL', 'ALLOW', 'ALMOST', 'ALONE', 'ALONG', 'ALREADY', 'ALRIGHT',
             'ALSO', 'ALTERNATIVE', 'ALTHOUGH', 'ALWAYS', 'AMONG', 'AMONGST', 'AMOUNT', 'AN', 'ANALYSIS', 'ANCIENT',
             'AND',
             'ANIMAL', 'ANNOUNCE', 'ANNUAL', 'ANOTHER', 'ANSWER', 'ANY', 'ANYBODY', 'ANYONE', 'ANYTHING', 'ANYWAY',
             'APART',
             'APPARENT', 'APPARENTLY', 'APPEAL', 'APPEAR', 'APPEARANCE', 'APPLICATION', 'APPLY', 'APPOINT',
             'APPOINTMENT',
             'APPROACH', 'APPROPRIATE', 'APPROVE', 'AREA', 'ARGUE', 'ARGUMENT', 'ARISE', 'ARM', 'ARMY', 'AROUND',
             'ARRANGE',
             'ARRANGEMENT', 'ARRIVE', 'ART', 'ARTICLE', 'ARTIST', 'AS', 'ASK', 'ASPECT', 'ASSEMBLY', 'ASSESS',
             'ASSESSMENT',
             'ASSET', 'ASSOCIATE', 'ASSOCIATION', 'ASSUME', 'ASSUMPTION', 'AT', 'ATMOSPHERE', 'ATTACH', 'ATTACK',
             'ATTEMPT',
             'ATTEND', 'ATTENTION', 'ATTITUDE', 'ATTRACT', 'ATTRACTIVE', 'AUDIENCE', 'AUTHOR', 'AUTHORITY', 'AVAILABLE',
             'AVERAGE', 'AVOID', 'AWARD', 'AWARE', 'AWAY', 'AYE', 'BABY', 'BACK', 'BACKGROUND', 'BAD', 'BAG', 'BALANCE',
             'BALL', 'BAND', 'BANK', 'BAR', 'BASE', 'BASIC', 'BASIS', 'BATTLE', 'BE', 'BEAR', 'BEAT', 'BEAUTIFUL',
             'BECAUSE', 'BECOME', 'BED', 'BEDROOM', 'BEFORE', 'BEGIN', 'BEGINNING', 'BEHAVIOUR', 'BEHIND', 'BELIEF',
             'BELIEVE', 'BELONG', 'BELOW', 'BENEATH', 'BENEFIT', 'BESIDE', 'BEST', 'BETTER', 'BETWEEN', 'BEYOND', 'BIG',
             'BILL', 'BIND', 'BIRD', 'BIRTH', 'BIT', 'BLACK', 'BLOCK', 'BLOOD', 'BLOODY', 'BLOW', 'BLUE', 'BOARD',
             'BOAT',
             'BODY', 'BONE', 'BOOK', 'BORDER', 'BOTH', 'BOTTLE', 'BOTTOM', 'BOX', 'BOY', 'BRAIN', 'BRANCH', 'BREAK',
             'BREATH', 'BRIDGE', 'BRIEF', 'BRIGHT', 'BRING', 'BROAD', 'BROTHER', 'BUDGET', 'BUILD', 'BUILDING', 'BURN',
             'BUS', 'BUSINESS', 'BUSY', 'BUT', 'BUY', 'BY', 'CABINET', 'CALL', 'CAMPAIGN', 'CAN', 'CANDIDATE',
             'CAPABLE',
             'CAPACITY', 'CAPITAL', 'CAR', 'CARD', 'CARE', 'CAREER', 'CAREFUL', 'CAREFULLY', 'CARRY', 'CASE', 'CASH',
             'CAT',
             'CATCH', 'CATEGORY', 'CAUSE', 'CELL', 'CENTRAL', 'CENTRE', 'CENTURY', 'CERTAIN', 'CERTAINLY', 'CHAIN',
             'CHAIR',
             'CHAIRMAN', 'CHALLENGE', 'CHANCE', 'CHANGE', 'CHANNEL', 'CHAPTER', 'CHARACTER', 'CHARACTERISTIC', 'CHARGE',
             'CHEAP', 'CHECK', 'CHEMICAL', 'CHIEF', 'CHILD', 'CHOICE', 'CHOOSE', 'CHURCH', 'CIRCLE', 'CIRCUMSTANCE',
             'CITIZEN', 'CITY', 'CIVIL', 'CLAIM', 'CLASS', 'CLEAN', 'CLEAR', 'CLEARLY', 'CLIENT', 'CLIMB', 'CLOSE',
             'CLOSELY', 'CLOTHES', 'CLUB', 'COAL', 'CODE', 'COFFEE', 'COLD', 'COLLEAGUE', 'COLLECT', 'COLLECTION',
             'COLLEGE', 'COLOUR', 'COMBINATION', 'COMBINE', 'COME', 'COMMENT', 'COMMERCIAL', 'COMMISSION', 'COMMIT',
             'COMMITMENT', 'COMMITTEE', 'COMMON', 'COMMUNICATION', 'COMMUNITY', 'COMPANY', 'COMPARE', 'COMPARISON',
             'COMPETITION', 'COMPLETE', 'COMPLETELY', 'COMPLEX', 'COMPONENT', 'COMPUTER', 'CONCENTRATE',
             'CONCENTRATION',
             'CONCEPT', 'CONCERN', 'CONCERNED', 'CONCLUDE', 'CONCLUSION', 'CONDITION', 'CONDUCT', 'CONFERENCE',
             'CONFIDENCE', 'CONFIRM', 'CONFLICT', 'CONGRESS', 'CONNECT', 'CONNECTION', 'CONSEQUENCE', 'CONSERVATIVE',
             'CONSIDER', 'CONSIDERABLE', 'CONSIDERATION', 'CONSIST', 'CONSTANT', 'CONSTRUCTION', 'CONSUMER', 'CONTACT',
             'CONTAIN', 'CONTENT', 'CONTEXT', 'CONTINUE', 'CONTRACT', 'CONTRAST', 'CONTRIBUTE', 'CONTRIBUTION',
             'CONTROL',
             'CONVENTION', 'CONVERSATION', 'COPY', 'CORNER', 'CORPORATE', 'CORRECT', 'COS', 'COST', 'COULD', 'COUNCIL',
             'COUNT', 'COUNTRY', 'COUNTY', 'COUPLE', 'COURSE', 'COURT', 'COVER', 'CREATE', 'CREATION', 'CREDIT',
             'CRIME',
             'CRIMINAL', 'CRISIS', 'CRITERION', 'CRITICAL', 'CRITICISM', 'CROSS', 'CROWD', 'CRY', 'CULTURAL', 'CULTURE',
             'CUP', 'CURRENT', 'CURRENTLY', 'CURRICULUM', 'CUSTOMER', 'CUT', 'DAMAGE', 'DANGER', 'DANGEROUS', 'DARK',
             'DATA', 'DATE', 'DAUGHTER', 'DAY', 'DEAD', 'DEAL', 'DEATH', 'DEBATE', 'DEBT', 'DECADE', 'DECIDE',
             'DECISION',
             'DECLARE', 'DEEP', 'DEFENCE', 'DEFENDANT', 'DEFINE', 'DEFINITION', 'DEGREE', 'DELIVER', 'DEMAND',
             'DEMOCRATIC',
             'DEMONSTRATE', 'DENY', 'DEPARTMENT', 'DEPEND', 'DEPUTY', 'DERIVE', 'DESCRIBE', 'DESCRIPTION', 'DESIGN',
             'DESIRE', 'DESK', 'DESPITE', 'DESTROY', 'DETAIL', 'DETAILED', 'DETERMINE', 'DEVELOP', 'DEVELOPMENT',
             'DEVICE',
             'DIE', 'DIFFERENCE', 'DIFFERENT', 'DIFFICULT', 'DIFFICULTY', 'DINNER', 'DIRECT', 'DIRECTION', 'DIRECTLY',
             'DIRECTOR', 'DISAPPEAR', 'DISCIPLINE', 'DISCOVER', 'DISCUSS', 'DISCUSSION', 'DISEASE', 'DISPLAY',
             'DISTANCE',
             'DISTINCTION', 'DISTRIBUTION', 'DISTRICT', 'DIVIDE', 'DIVISION', 'DO', 'DOCTOR', 'DOCUMENT', 'DOG',
             'DOMESTIC',
             'DOOR', 'DOUBLE', 'DOUBT', 'DOWN', 'DRAW', 'DRAWING', 'DREAM', 'DRESS', 'DRINK', 'DRIVE', 'DRIVER', 'DROP',
             'DRUG', 'DRY', 'DUE', 'DURING', 'DUTY', 'EACH', 'EAR', 'EARLY', 'EARN', 'EARTH', 'EASILY', 'EAST', 'EASY',
             'EAT', 'ECONOMIC', 'ECONOMY', 'EDGE', 'EDITOR', 'EDUCATION', 'EDUCATIONAL', 'EFFECT', 'EFFECTIVE',
             'EFFECTIVELY', 'EFFORT', 'EGG', 'EITHER', 'ELDERLY', 'ELECTION', 'ELEMENT', 'ELSE', 'ELSEWHERE', 'EMERGE',
             'EMPHASIS', 'EMPLOY', 'EMPLOYEE', 'EMPLOYER', 'EMPLOYMENT', 'EMPTY', 'ENABLE', 'ENCOURAGE', 'END', 'ENEMY',
             'ENERGY', 'ENGINE', 'ENGINEERING', 'ENJOY', 'ENOUGH', 'ENSURE', 'ENTER', 'ENTERPRISE', 'ENTIRE',
             'ENTIRELY',
             'ENTITLE', 'ENTRY', 'ENVIRONMENT', 'ENVIRONMENTAL', 'EQUAL', 'EQUALLY', 'EQUIPMENT', 'ERROR', 'ESCAPE',
             'ESPECIALLY', 'ESSENTIAL', 'ESTABLISH', 'ESTABLISHMENT', 'ESTATE', 'ESTIMATE', 'EVEN', 'EVENING', 'EVENT',
             'EVENTUALLY', 'EVER', 'EVERY', 'EVERYBODY', 'EVERYONE', 'EVERYTHING', 'EVIDENCE', 'EXACTLY', 'EXAMINATION',
             'EXAMINE', 'EXAMPLE', 'EXCELLENT', 'EXCEPT', 'EXCHANGE', 'EXECUTIVE', 'EXERCISE', 'EXHIBITION', 'EXIST',
             'EXISTENCE', 'EXISTING', 'EXPECT', 'EXPECTATION', 'EXPENDITURE', 'EXPENSE', 'EXPENSIVE', 'EXPERIENCE',
             'EXPERIMENT', 'EXPERT', 'EXPLAIN', 'EXPLANATION', 'EXPLORE', 'EXPRESS', 'EXPRESSION', 'EXTEND', 'EXTENT',
             'EXTERNAL', 'EXTRA', 'EXTREMELY', 'EYE', 'FACE', 'FACILITY', 'FACT', 'FACTOR', 'FACTORY', 'FAIL',
             'FAILURE',
             'FAIR', 'FAIRLY', 'FAITH', 'FALL', 'FAMILIAR', 'FAMILY', 'FAMOUS', 'FAR', 'FARM', 'FARMER', 'FASHION',
             'FAST',
             'FATHER', 'FAVOUR', 'FEAR', 'FEATURE', 'FEE', 'FEEL', 'FEELING', 'FEMALE', 'FEW', 'FIELD', 'FIGHT',
             'FIGURE',
             'FILE', 'FILL', 'FILM', 'FINAL', 'FINALLY', 'FINANCE', 'FINANCIAL', 'FIND', 'FINDING', 'FINE', 'FINGER',
             'FINISH', 'FIRE', 'FIRM', 'FIRST', 'FISH', 'FIT', 'FIX', 'FLAT', 'FLIGHT', 'FLOOR', 'FLOW', 'FLOWER',
             'FLY',
             'FOCUS', 'FOLLOW', 'FOLLOWING', 'FOOD', 'FOOT', 'FOOTBALL', 'FOR', 'FORCE', 'FOREIGN', 'FOREST', 'FORGET',
             'FORM', 'FORMAL', 'FORMER', 'FORWARD', 'FOUNDATION', 'FREE', 'FREEDOM', 'FREQUENTLY', 'FRESH', 'FRIEND',
             'FROM', 'FRONT', 'FRUIT', 'FUEL', 'FULL', 'FULLY', 'FUNCTION', 'FUND', 'FUNNY', 'FURTHER', 'FUTURE',
             'GAIN',
             'GAME', 'GARDEN', 'GAS', 'GATE', 'GATHER', 'GENERAL', 'GENERALLY', 'GENERATE', 'GENERATION', 'GENTLEMAN',
             'GET', 'GIRL', 'GIVE', 'GLASS', 'GO', 'GOAL', 'GOD', 'GOLD', 'GOOD', 'GOVERNMENT', 'GRANT', 'GREAT',
             'GREEN',
             'GREY', 'GROUND', 'GROUP', 'GROW', 'GROWING', 'GROWTH', 'GUEST', 'GUIDE', 'GUN', 'HAIR', 'HALF', 'HALL',
             'HAND', 'HANDLE', 'HANG', 'HAPPEN', 'HAPPY', 'HARD', 'HARDLY', 'HATE', 'HAVE', 'HE', 'HEAD', 'HEALTH',
             'HEAR',
             'HEART', 'HEAT', 'HEAVY', 'HELL', 'HELP', 'HENCE', 'HER', 'HERE', 'HERSELF', 'HIDE', 'HIGH', 'HIGHLY',
             'HILL',
             'HIM', 'HIMSELF', 'HIS', 'HISTORICAL', 'HISTORY', 'HIT', 'HOLD', 'HOLE', 'HOLIDAY', 'HOME', 'HOPE',
             'HORSE',
             'HOSPITAL', 'HOT', 'HOTEL', 'HOUR', 'HOUSE', 'HOUSEHOLD', 'HOUSING', 'HOW', 'HOWEVER', 'HUGE', 'HUMAN',
             'HURT',
             'HUSBAND', 'I', 'IDEA', 'IDENTIFY', 'IF', 'IGNORE', 'ILLUSTRATE', 'IMAGE', 'IMAGINE', 'IMMEDIATE',
             'IMMEDIATELY', 'IMPACT', 'IMPLICATION', 'IMPLY', 'IMPORTANCE', 'IMPORTANT', 'IMPOSE', 'IMPOSSIBLE',
             'IMPRESSION', 'IMPROVE', 'IMPROVEMENT', 'IN', 'INCIDENT', 'INCLUDE', 'INCLUDING', 'INCOME', 'INCREASE',
             'INCREASED', 'INCREASINGLY', 'INDEED', 'INDEPENDENT', 'INDEX', 'INDICATE', 'INDIVIDUAL', 'INDUSTRIAL',
             'INDUSTRY', 'INFLUENCE', 'INFORM', 'INFORMATION', 'INITIAL', 'INITIATIVE', 'INJURY', 'INSIDE', 'INSIST',
             'INSTANCE', 'INSTEAD', 'INSTITUTE', 'INSTITUTION', 'INSTRUCTION', 'INSTRUMENT', 'INSURANCE', 'INTEND',
             'INTENTION', 'INTEREST', 'INTERESTED', 'INTERESTING', 'INTERNAL', 'INTERNATIONAL', 'INTERPRETATION',
             'INTERVIEW', 'INTO', 'INTRODUCE', 'INTRODUCTION', 'INVESTIGATE', 'INVESTIGATION', 'INVESTMENT', 'INVITE',
             'INVOLVE', 'IRON', 'IS', 'ISLAND', 'ISSUE', 'IT', 'ITEM', 'ITS', 'ITSELF', 'JOB', 'JOIN', 'JOINT',
             'JOURNEY',
             'JUDGE', 'JUMP', 'JUST', 'JUSTICE', 'KEEP', 'KEY', 'KID', 'KILL', 'KIND', 'KING', 'KITCHEN', 'KNEE',
             'KNOW',
             'KNOWLEDGE', 'LABOUR', 'LACK', 'LADY', 'LAND', 'LANGUAGE', 'LARGE', 'LARGELY', 'LAST', 'LATE', 'LATER',
             'LATTER', 'LAUGH', 'LAUNCH', 'LAW', 'LAWYER', 'LAY', 'LEAD', 'LEADER', 'LEADERSHIP', 'LEADING', 'LEAF',
             'LEAGUE', 'LEAN', 'LEARN', 'LEAST', 'LEAVE', 'LEFT', 'LEG', 'LEGAL', 'LEGISLATION', 'LENGTH', 'LESS',
             'LET',
             'LETTER', 'LEVEL', 'LIABILITY', 'LIBERAL', 'LIBRARY', 'LIE', 'LIFE', 'LIFT', 'LIGHT', 'LIKE', 'LIKELY',
             'LIMIT', 'LIMITED', 'LINE', 'LINK', 'LIP', 'LIST', 'LISTEN', 'LITERATURE', 'LITTLE', 'LIVE', 'LIVING',
             'LOAN',
             'LOCAL', 'LOCATION', 'LONG', 'LOOK', 'LORD', 'LOSE', 'LOSS', 'LOT', 'LOVE', 'LOVELY', 'LOW', 'LUNCH',
             'MACHINE', 'MAGAZINE', 'MAIN', 'MAINLY', 'MAINTAIN', 'MAJOR', 'MAJORITY', 'MAKE', 'MALE', 'MAN', 'MANAGE',
             'MANAGEMENT', 'MANAGER', 'MANNER', 'MANY', 'MAP', 'MARK', 'MARKET', 'MARRIAGE', 'MARRIED', 'MARRY', 'MASS',
             'MASTER', 'MATCH', 'MATERIAL', 'MATTER', 'MAY', 'MAYBE', 'ME', 'MEAL', 'MEAN', 'MEANING', 'MEANS',
             'MEANWHILE',
             'MEASURE', 'MECHANISM', 'MEDIA', 'MEDICAL', 'MEET', 'MEETING', 'MEMBER', 'MEMBERSHIP', 'MEMORY', 'MENTAL',
             'MENTION', 'MERELY', 'MESSAGE', 'METAL', 'METHOD', 'MIDDLE', 'MIGHT', 'MILE', 'MILITARY', 'MILK', 'MIND',
             'MINE', 'MINISTER', 'MINISTRY', 'MINUTE', 'MISS', 'MISTAKE', 'MODEL', 'MODERN', 'MODULE', 'MOMENT',
             'MONEY',
             'MONTH', 'MORE', 'MORNING', 'MOST', 'MOTHER', 'MOTION', 'MOTOR', 'MOUNTAIN', 'MOUTH', 'MOVE', 'MOVEMENT',
             'MUCH', 'MURDER', 'MUSEUM', 'MUSIC', 'MUST', 'MY', 'MYSELF', 'NAME', 'NARROW', 'NATION', 'NATIONAL',
             'NATURAL',
             'NATURE', 'NEAR', 'NEARLY', 'NECESSARILY', 'NECESSARY', 'NECK', 'NEED', 'NEGOTIATION', 'NEIGHBOUR',
             'NEITHER',
             'NETWORK', 'NEVER', 'NEVERTHELESS', 'NEW', 'NEWS', 'NEWSPAPER', 'NEXT', 'NICE', 'NIGHT', 'NO', 'NOBODY',
             'NOD',
             'NOISE', 'NONE', 'NOR', 'NORMAL', 'NORMALLY', 'NORTH', 'NORTHERN', 'NOSE', 'NOT', 'NOTE', 'NOTHING',
             'NOTICE',
             'NOTION', 'NOW', 'NUCLEAR', 'NUMBER', 'NURSE', 'OBJECT', 'OBJECTIVE', 'OBSERVATION', 'OBSERVE', 'OBTAIN',
             'OBVIOUS', 'OBVIOUSLY', 'OCCASION', 'OCCUR', 'ODD', 'OF', 'OFF', 'OFFENCE', 'OFFER', 'OFFICE', 'OFFICER',
             'OFFICIAL', 'OFTEN', 'OIL', 'OKAY', 'OLD', 'ON', 'ONCE', 'ONE', 'ONLY', 'ONTO', 'OPEN', 'OPERATE',
             'OPERATION',
             'OPINION', 'OPPORTUNITY', 'OPPOSITION', 'OPTION', 'OR', 'ORDER', 'ORDINARY', 'ORGANISATION', 'ORGANISE',
             'ORGANIZATION', 'ORIGIN', 'ORIGINAL', 'OTHER', 'OTHERWISE', 'OUGHT', 'OUR', 'OURSELVES', 'OUT', 'OUTCOME',
             'OUTPUT', 'OUTSIDE', 'OVER', 'OVERALL', 'OWN', 'OWNER', 'PACKAGE', 'PAGE', 'PAIN', 'PAINT', 'PAINTING',
             'PAIR',
             'PANEL', 'PAPER', 'PARENT', 'PARK', 'PARLIAMENT', 'PART', 'PARTICULAR', 'PARTICULARLY', 'PARTLY',
             'PARTNER',
             'PARTY', 'PASS', 'PASSAGE', 'PAST', 'PATH', 'PATIENT', 'PATTERN', 'PAY', 'PAYMENT', 'PEACE', 'PENSION',
             'PEOPLE', 'PER', 'PERCENT', 'PERFECT', 'PERFORM', 'PERFORMANCE', 'PERHAPS', 'PERIOD', 'PERMANENT',
             'PERSON',
             'PERSONAL', 'PERSUADE', 'PHASE', 'PHONE', 'PHOTOGRAPH', 'PHYSICAL', 'PICK', 'PICTURE', 'PIECE', 'PLACE',
             'PLAN', 'PLANNING', 'PLANT', 'PLASTIC', 'PLATE', 'PLAY', 'PLAYER', 'PLEASE', 'PLEASURE', 'PLENTY', 'PLUS',
             'POCKET', 'POINT', 'POLICE', 'POLICY', 'POLITICAL', 'POLITICS', 'POOL', 'POOR', 'POPULAR', 'POPULATION',
             'POSITION', 'POSITIVE', 'POSSIBILITY', 'POSSIBLE', 'POSSIBLY', 'POST', 'POTENTIAL', 'POUND', 'POWER',
             'POWERFUL', 'PRACTICAL', 'PRACTICE', 'PREFER', 'PREPARE', 'PRESENCE', 'PRESENT', 'PRESIDENT', 'PRESS',
             'PRESSURE', 'PRETTY', 'PREVENT', 'PREVIOUS', 'PREVIOUSLY', 'PRICE', 'PRIMARY', 'PRIME', 'PRINCIPLE',
             'PRIORITY', 'PRISON', 'PRISONER', 'PRIVATE', 'PROBABLY', 'PROBLEM', 'PROCEDURE', 'PROCESS', 'PRODUCE',
             'PRODUCT', 'PRODUCTION', 'PROFESSIONAL', 'PROFIT', 'PROGRAM', 'PROGRAMME', 'PROGRESS', 'PROJECT',
             'PROMISE',
             'PROMOTE', 'PROPER', 'PROPERLY', 'PROPERTY', 'PROPORTION', 'PROPOSE', 'PROPOSAL', 'PROSPECT', 'PROTECT',
             'PROTECTION', 'PROVE', 'PROVIDE', 'PROVIDED', 'PROVISION', 'PUB', 'PUBLIC', 'PUBLICATION', 'PUBLISH',
             'PULL',
             'PUPIL', 'PURPOSE', 'PUSH', 'PUT', 'QUALITY', 'QUARTER', 'QUESTION', 'QUICK', 'QUICKLY', 'QUIET', 'QUITE',
             'RACE', 'RADIO', 'RAILWAY', 'RAIN', 'RAISE', 'RANGE', 'RAPIDLY', 'RARE', 'RATE', 'RATHER', 'REACH',
             'REACTION',
             'READ', 'READER', 'READING', 'READY', 'REAL', 'REALISE', 'REALITY', 'REALIZE', 'REALLY', 'REASON',
             'REASONABLE', 'RECALL', 'RECEIVE', 'RECENT', 'RECENTLY', 'RECOGNISE', 'RECOGNITION', 'RECOGNIZE',
             'RECOMMEND',
             'RECORD', 'RECOVER', 'RED', 'REDUCE', 'REDUCTION', 'REFER', 'REFERENCE', 'REFLECT', 'REFORM', 'REFUSE',
             'REGARD', 'REGION', 'REGIONAL', 'REGULAR', 'REGULATION', 'REJECT', 'RELATE', 'RELATION', 'RELATIONSHIP',
             'RELATIVE', 'RELATIVELY', 'RELEASE', 'RELEVANT', 'RELIEF', 'RELIGION', 'RELIGIOUS', 'RELY', 'REMAIN',
             'REMEMBER', 'REMIND', 'REMOVE', 'REPEAT', 'REPLACE', 'REPLY', 'REPORT', 'REPRESENT', 'REPRESENTATION',
             'REPRESENTATIVE', 'REQUEST', 'REQUIRE', 'REQUIREMENT', 'RESEARCH', 'RESOURCE', 'RESPECT', 'RESPOND',
             'RESPONSE', 'RESPONSIBILITY', 'RESPONSIBLE', 'REST', 'RESTAURANT', 'RESULT', 'RETAIN', 'RETURN', 'REVEAL',
             'REVENUE', 'REVIEW', 'REVOLUTION', 'RICH', 'RIDE', 'RIGHT', 'RING', 'RISE', 'RISK', 'RIVER', 'ROAD',
             'ROCK',
             'ROLE', 'ROLL', 'ROOF', 'ROOM', 'ROUND', 'ROUTE', 'ROW', 'ROYAL', 'RULE', 'RUN', 'RURAL', 'SAFE', 'SAFETY',
             'SALE', 'SAME', 'SAMPLE', 'SATISFY', 'SAVE', 'SAY', 'SCALE', 'SCENE', 'SCHEME', 'SCHOOL', 'SCIENCE',
             'SCIENTIFIC', 'SCIENTIST', 'SCORE', 'SCREEN', 'SEA', 'SEARCH', 'SEASON', 'SEAT', 'SECOND', 'SECONDARY',
             'SECRETARY', 'SECTION', 'SECTOR', 'SECURE', 'SECURITY', 'SEE', 'SEEK', 'SEEM', 'SELECT', 'SELECTION',
             'SELL',
             'SEND', 'SENIOR', 'SENSE', 'SENTENCE', 'SEPARATE', 'SEQUENCE', 'SERIES', 'SERIOUS', 'SERIOUSLY', 'SERVANT',
             'SERVE', 'SERVICE', 'SESSION', 'SET', 'SETTLE', 'SETTLEMENT', 'SEVERAL', 'SEVERE', 'SEX', 'SEXUAL',
             'SHAKE',
             'SHALL', 'SHAPE', 'SHARE', 'SHE', 'SHEET', 'SHIP', 'SHOE', 'SHOOT', 'SHOP', 'SHORT', 'SHOT', 'SHOULD',
             'SHOULDER', 'SHOUT', 'SHOW', 'SHUT', 'SIDE', 'SIGHT', 'SIGN', 'SIGNAL', 'SIGNIFICANCE', 'SIGNIFICANT',
             'SILENCE', 'SIMILAR', 'SIMPLE', 'SIMPLY', 'SINCE', 'SING', 'SINGLE', 'SIR', 'SISTER', 'SIT', 'SITE',
             'SITUATION', 'SIZE', 'SKILL', 'SKIN', 'SKY', 'SLEEP', 'SLIGHTLY', 'SLIP', 'SLOW', 'SLOWLY', 'SMALL',
             'SMILE',
             'SO', 'SOCIAL', 'SOCIETY', 'SOFT', 'SOFTWARE', 'SOIL', 'SOLDIER', 'SOLICITOR', 'SOLUTION', 'SOME',
             'SOMEBODY',
             'SOMEONE', 'SOMETHING', 'SOMETIMES', 'SOMEWHAT', 'SOMEWHERE', 'SON', 'SONG', 'SOON', 'SORRY', 'SORT',
             'SOUND',
             'SOURCE', 'SOUTH', 'SOUTHERN', 'SPACE', 'SPEAK', 'SPEAKER', 'SPECIAL', 'SPECIES', 'SPECIFIC', 'SPEECH',
             'SPEED', 'SPEND', 'SPIRIT', 'SPORT', 'SPOT', 'SPREAD', 'SPRING', 'STAFF', 'STAGE', 'STAND', 'STANDARD',
             'STAR',
             'START', 'STATE', 'STATEMENT', 'STATION', 'STATUS', 'STAY', 'STEAL', 'STEP', 'STICK', 'STILL', 'STOCK',
             'STONE', 'STOP', 'STORE', 'STORY', 'STRAIGHT', 'STRANGE', 'STRATEGY', 'STREET', 'STRENGTH', 'STRIKE',
             'STRONG',
             'STRONGLY', 'STRUCTURE', 'STUDENT', 'STUDIO', 'STUDY', 'STUFF', 'STYLE', 'SUBJECT', 'SUBSTANTIAL',
             'SUCCEED',
             'SUCCESS', 'SUCCESSFUL', 'SUCH', 'SUDDENLY', 'SUFFER', 'SUFFICIENT', 'SUGGEST', 'SUGGESTION', 'SUITABLE',
             'SUM', 'SUMMER', 'SUN', 'SUPPLY', 'SUPPORT', 'SUPPOSE', 'SURE', 'SURELY', 'SURFACE', 'SURPRISE',
             'SURROUND',
             'SURVEY', 'SURVIVE', 'SWITCH', 'SYSTEM', 'TABLE', 'TAKE', 'TALK', 'TALL', 'TAPE', 'TARGET', 'TASK', 'TAX',
             'TEA', 'TEACH', 'TEACHER', 'TEACHING', 'TEAM', 'TEAR', 'TECHNICAL', 'TECHNIQUE', 'TECHNOLOGY', 'TELEPHONE',
             'TELEVISION', 'TELL', 'TEMPERATURE', 'TEND', 'TERM', 'TERMS', 'TERRIBLE', 'TEST', 'TEXT', 'THAN', 'THANK',
             'THANKS', 'THAT', 'THE', 'THEATRE', 'THEIR', 'THEM', 'THEME', 'THEMSELVES', 'THEN', 'THEORY', 'THERE',
             'THEREFORE', 'THESE', 'THEY', 'THIN', 'THING', 'THINK', 'THIS', 'THOSE', 'THOUGH', 'THOUGHT', 'THREAT',
             'THREATEN', 'THROUGH', 'THROUGHOUT', 'THROW', 'THUS', 'TICKET', 'TIME', 'TINY', 'TITLE', 'TO', 'TODAY',
             'TOGETHER', 'TOMORROW', 'TONE', 'TONIGHT', 'TOO', 'TOOL', 'TOOTH', 'TOP', 'TOTAL', 'TOTALLY', 'TOUCH',
             'TOUR',
             'TOWARDS', 'TOWN', 'TRACK', 'TRADE', 'TRADITION', 'TRADITIONAL', 'TRAFFIC', 'TRAIN', 'TRAINING',
             'TRANSFER',
             'TRANSPORT', 'TRAVEL', 'TREAT', 'TREATMENT', 'TREATY', 'TREE', 'TREND', 'TRIAL', 'TRIP', 'TROOP',
             'TROUBLE',
             'TRUE', 'TRUST', 'TRUTH', 'TRY', 'TURN', 'TWICE', 'TYPE', 'TYPICAL', 'UNABLE', 'UNDER', 'UNDERSTAND',
             'UNDERSTANDING', 'UNDERTAKE', 'UNEMPLOYMENT', 'UNFORTUNATELY', 'UNION', 'UNIT', 'UNITED', 'UNIVERSITY',
             'UNLESS', 'UNLIKELY', 'UNTIL', 'UP', 'UPON', 'UPPER', 'URBAN', 'US', 'USE', 'USED', 'USEFUL', 'USER',
             'USUAL',
             'USUALLY', 'VALUE', 'VARIATION', 'VARIETY', 'VARIOUS', 'VARY', 'VAST', 'VEHICLE', 'VERSION', 'VERY', 'VIA',
             'VICTIM', 'VICTORY', 'VIDEO', 'VIEW', 'VILLAGE', 'VIOLENCE', 'VISION', 'VISIT', 'VISITOR', 'VITAL',
             'VOICE',
             'VOLUME', 'VOTE', 'WAGE', 'WAIT', 'WALK', 'WALL', 'WANT', 'WAR', 'WARM', 'WARN', 'WASH', 'WATCH', 'WATER',
             'WAVE', 'WAY', 'WE', 'WEAK', 'WEAPON', 'WEAR', 'WEATHER', 'WEEK', 'WEEKEND', 'WEIGHT', 'WELCOME',
             'WELFARE',
             'WELL', 'WEST', 'WESTERN', 'WHAT', 'WHATEVER', 'WHEN', 'WHERE', 'WHEREAS', 'WHETHER', 'WHICH', 'WHILE',
             'WHILST', 'WHITE', 'WHO', 'WHOLE', 'WHOM', 'WHOSE', 'WHY', 'WIDE', 'WIDELY', 'WIFE', 'WILD', 'WILL', 'WIN',
             'WIND', 'WINDOW', 'WINE', 'WING', 'WINNER', 'WINTER', 'WISH', 'WITH', 'WITHDRAW', 'WITHIN', 'WITHOUT',
             'WOMAN',
             'WONDER', 'WONDERFUL', 'WOOD', 'WORD', 'WORK', 'WORKER', 'WORKING', 'WORKS', 'WORLD', 'WORRY', 'WORTH',
             'WOULD', 'WRITE', 'WRITER', 'WRITING', 'WRONG', 'YARD', 'YEAH', 'YEAR', 'YES', 'YESTERDAY', 'YET', 'YOU',
             'YOUNG', 'YOUR', 'YOURSELF', 'YOUTH']
    classe = words[:]
    listanagrams = []
    maximum = 0

    for k in range(0, len(words)):
        classe[k] = ordonnemot(classe[k])

    for a in range(0, len(words)):
        for b in range(a + 1, len(words)):
            if classe[a] == classe[b]:
                listanagrams.append([words[a], words[b]])

    for a in listanagrams:
        lettres = set(a[0])
        for b in itertools.permutations('123456789', len(lettres)):
            keys = list(lettres)
            values = list(b)
            alphabet = dict(zip(keys, values))
            nombre1 = replace_all(a[0], alphabet)
            nombre2 = replace_all(a[1], alphabet)
            if issqr(int(nombre1)) and issqr(int(nombre2)):
                maximum = max(maximum, int(nombre1), int(nombre2))

    print(maximum)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())