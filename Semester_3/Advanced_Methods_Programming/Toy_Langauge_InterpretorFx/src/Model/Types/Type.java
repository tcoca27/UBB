package Model.Types;

import Model.Values.Value;

public interface Type {
    boolean equals(Object other);
    Value defaultVal();
}
